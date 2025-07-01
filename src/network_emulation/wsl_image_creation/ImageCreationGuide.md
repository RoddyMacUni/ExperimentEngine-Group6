# Netem enabled operating system image creation guide
This document will detail how the image used to run the experiments on a virtual network was created. Arch was selected as the base for this image due to the extensive documentation and easy to use build system. A pre-built WSL image can be found at [this link](https://strath-my.sharepoint.com/:u:/g/personal/roderick_macrae_2022_uni_strath_ac_uk/Ef1uouMlUO9Mh3yVYqhoBIIBtfMMTODno79M7zRD1OzJ3Q?e=qbe0Nk)

## 1. Kernel compilation

Note: These steps are largely taken from the documentation and adapted to suit the needs of this project, the documentation can be found [here](https://wiki.archlinux.org/title/Kernel/Arch_build_system)
1. Arch environment created with correct permissions
2. Followed [instructions](https://wiki.archlinux.org/title/Kernel/Arch_build_system#) from 1.0 → 2.2
3. Executed `makepkg -s --skippgpcheck` - Takes a long time to run
4. Kernel created

## 2. Disc image (ISO) creation
1. Installed archiso  
   a. `sudo pacman -S archiso`
2. Copy the monthly release ISO profile  
   a. `cp -r /usr/share/archiso/configs/releng/ netem-enabled-arch`
3. Move `/boot/vmlinuz-netem-enabled-arch` to `~/netem-enabled-arch/airootfs/boot/`
4. Move `/boot/initramfs-netem-enabled-arch.img` to `~/netem-enabled-arch/boot/`
5. Rename `~/netem-enabled-arch/airootfs/etc/mkinitcpio.d/linux-lts.preset` to `netem-enabled-arch.preset`
6. Open and amend `netem-enabled-arch.preset`<br>
   a. Set ALL_kver to `'/boot/vmlinuz-netem-enabled-arch'`<br>
   b. Set archiso_image to `"/boot/initramfs-netem-enabled-arch.img"`<br>
7. Run `sudo mkarchiso -v -w /tmp/netem-enabled-arch -o ~ netem-enabled-arch` to build the iso file
8. ISO image created

## 3. WSL container creation

Source: [Microsoft WSL Distro creation guide](https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro)

1. Mount the ISO to a working arch instance and extract the squashfs root file system  
   `mkdir /mnt/ne-arch`  
   `mount ~/netem-enabled-arch.iso /mnt/ne-arch`  
   `mkdir ~/ne-arch-squashfs`  
   `cp /mnt/ne-arch/arch/x86_64/airootfs.sfs ~/ne-arch-squashfs`  
   `cd ~/ne-arch-squashfs`  
   `unsquash ~/ne-arch-squashfs/airootfs.sfs`  
3. Add the /etc/wsl.conf and /etc/wsl-distribution.conf file
4. Add the files referred to in the two wsl configuration files to the /usr/lib/wsl/ directory
5. Compress the root filesystem to a .tar.gz file  
   `cd ~/netem-enabled-arch/squashfs-root/`  
   `sudo tar --numeric-owner --absolute-names -c  * | gzip --best > ../ne-arch.tar.gz`  
6. Copy the root filesystem to the windows mount and rename to .wsl
   `mv ../install.tar.gz ../ne-arch.wsl`  
   `cp ~/netem-enabled-arch/ne-arch.wsl /mnt/c/User/<username>/`  
7. WSL image created
