#! /bin/bash

# ExperimentEngine-Group6 reports to STDOUT so this replicates that
cat << MOCK_STREAM_DATA_STDOUT > /dev/stdout
[EE_INFO] Sequence_number 1
[EE_INFO] Delay: 11
[EE_INFO] Packet Loss: 9
[EE_INFO] Source file: /tmp/sample_source.mp4
[EE_INFO] Distorted file path: /tmp/1-1-disrupted.mp4
[EE_INFO] Enabling sch_netem
[EE_INFO] Applying network conditions
[EE_INFO] Deleting previously exported file
[EE_INFO] Creating sdp file
[EE_INFO] Starting stream
MOCK_STREAM_DATA_STDOUT

# FFMPEG outputs to STDERR by default so this replicates that
cat << MOCK_STREAM_DATA_STDERR > /dev/stderr
Error: Exclusivity flag on, cannot modify.
ffmpeg version n7.1.1 Copyright (c) 2000-2025 the FFmpeg developers
  built with gcc 15.1.1 (GCC) 20250425
  configuration: --prefix=/usr --disable-debug --disable-static --disable-stripping --enable-amf --enable-avisynth --enable-cuda-llvm --enable-lto --enable-fontconfig --enable-frei0r --enable-gmp --enable-gnutls --enable-gpl --enable-ladspa --enable-libaom --enable-libass --enable-libbluray --enable-libbs2b --enable-libdav1d --enable-libdrm --enable-libdvdnav --enable-libdvdread --enable-libfreetype --enable-libfribidi --enable-libglslang --enable-libgsm --enable-libharfbuzz --enable-libiec61883 --enable-libjack --enable-libjxl --enable-libmodplug --enable-libmp3lame --enable-libopencore_amrnb --enable-libopencore_amrwb --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libplacebo --enable-libpulse --enable-librav1e --enable-librsvg --enable-librubberband --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtheora --enable-libv4l2 --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpl --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxcb --enable-libxml2 --enable-libxvid --enable-libzimg --enable-libzmq --enable-nvdec --enable-nvenc --enable-opencl --enable-opengl --enable-shared --enable-vapoursynth --enable-version3 --enable-vulkan
ffmpeg version n7.1.1 Copyright (c) 2000-2025 the FFmpeg developers
  built with gcc 15.1.1 (GCC) 20250425
  configuration: --prefix=/usr --disable-debug --disable-static --disable-stripping --enable-amf --enable-avisynth --enable-cuda-llvm --enable-lto --enable-fontconfig --enable-frei0r --enable-gmp --enable-gnutls --enable-gpl --enable-ladspa --enable-libaom --enable-libass --enable-libbluray --enable-libbs2b --enable-libdav1d --enable-libdrm --enable-libdvdnav --enable-libdvdread --enable-libfreetype --enable-libfribidi --enable-libglslang --enable-libgsm --enable-libharfbuzz --enable-libiec61883 --enable-libjack --enable-libjxl --enable-libmodplug --enable-libmp3lame --enable-libopencore_amrnb --enable-libopencore_amrwb --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libplacebo --enable-libpulse --enable-librav1e --enable-librsvg --enable-librubberband --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtheora --enable-libv4l2 --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpl --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxcb --enable-libxml2 --enable-libxvid --enable-libzimg --enable-libzmq --enable-nvdec --enable-nvenc --enable-opencl --enable-opengl --enable-shared --enable-vapoursynth --enable-version3 --enable-vulkan
  libavutil      59. 39.100 / 59. 39.100
  libavcodec     61. 19.101 / 61. 19.101
  libavformat    61.  7.100 / 61.  7.100
  libavdevice    61.  3.100 / 61.  3.100
  libavfilter    10.  4.100 / 10.  4.100
  libswscale      8.  3.100 /  8.  3.100
  libswresample   5.  3.100 /  5.  3.100
  libpostproc    58.  3.100 / 58.  3.100
  libavutil      59. 39.100 / 59. 39.100
  libavcodec     61. 19.101 / 61. 19.101
  libavformat    61.  7.100 / 61.  7.100
  libavdevice    61.  3.100 / 61.  3.100
  libavfilter    10.  4.100 / 10.  4.100
  libswscale      8.  3.100 /  8.  3.100
  libswresample   5.  3.100 /  5.  3.100
  libpostproc    58.  3.100 / 58.  3.100
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from '/tmp/sample_source.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2mp41
    encoder         : Lavf62.0.100
  Duration: 00:00:10.01, start: 0.000000, bitrate: 514 kb/s
  Stream #0:0[0x1](und): Video: hevc (Main) (hev1 / 0x31766568), yuv420p(tv, progressive), 352x288 [SAR 128:117 DAR 1408:1053], 508 kb/s, 29.97 fps, 29.97 tbr, 30k tbn (default)
      Metadata:
        handler_name    : VideoHandler
        vendor_id       : [0][0][0][0]
        encoder         : Lavc62.0.101 libx265
Stream mapping:
  Stream #0:0 -> #0:0 (copy)
Output #0, rtp, to 'rtp://127.0.0.1:1234':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2mp41
    encoder         : Lavf61.7.100
  Stream #0:0(und): Video: hevc (Main) (hev1 / 0x31766568), yuv420p(tv, progressive), 352x288 [SAR 128:117 DAR 1408:1053], q=2-31, 508 kb/s, 29.97 fps, 29.97 tbr, 90k tbn (default)
      Metadata:
        handler_name    : VideoHandler
        vendor_id       : [0][0][0][0]
        encoder         : Lavc62.0.101 libx265
Press [q] to stop, [?] for help
Input #0, sdp, from '/tmp/experiment.sdp':
  Metadata:
    title           : No Name
  Duration: N/A, start: 0.233567, bitrate: N/A
  Stream #0:0: Video: hevc (Main), yuv420p(tv), 352x288 [SAR 128:117 DAR 1408:1053], 29.97 fps, 29.97 tbr, 90k tbn
Stream mapping:
  Stream #0:0 -> #0:0 (hevc (native) -> h264 (libx264))
Press [q] to stop, [?] for help
[libx264 @ 0x58fa7594ac80] using SAR=128/117
[libx264 @ 0x58fa7594ac80] using cpu capabilities: MMX2 SSE2Fast SSSE3 SSE4.2 AVX FMA3 BMI2 AVX2 AVX512
[libx264 @ 0x58fa7594ac80] profile High, level 1.3, 4:2:0, 8-bit
[libx264 @ 0x58fa7594ac80] 264 - core 164 r3108 31e19f9 - H.264/MPEG-4 AVC codec - Copyleft 2003-2023 - http://www.videolan.org/x264.html - options: cabac=1 ref=3 deblock=1:0:0 analyse=0x3:0x113 me=hex subme=7 psy=1 psy_rd=1.00:0.00 mixed_ref=1 me_range=16 chroma_me=1 trellis=1 8x8dct=1 cqm=0 deadzone=21,11 fast_pskip=1 chroma_qp_offset=-2 threads=9 lookahead_threads=1 sliced_threads=0 nr=0 decimate=1 interlaced=0 bluray_compat=0 constrained_intra=0 bframes=3 b_pyramid=2 b_adapt=1 b_bias=0 direct=1 weightb=1 open_gop=0 weightp=2 keyint=250 keyint_min=25 scenecut=40 intra_refresh=0 rc_lookahead=40 rc=crf mbtree=1 crf=23.0 qcomp=0.60 qpmin=0 qpmax=69 qpstep=4 ip_ratio=1.40 aq=1:1.00
Output #0, mp4, to '/tmp/1-1-disrupted.mp4':
  Metadata:
    title           : No Name
    encoder         : Lavf61.7.100
  Stream #0:0: Video: h264 (avc1 / 0x31637661), yuv420p(tv, progressive), 352x288 [SAR 128:117 DAR 1408:1053], q=2-31, 29.97 fps, 30k tbn
      Metadata:
        encoder         : Lavc61.19.101 libx264
      Side data:
        cpb: bitrate max/min/avg: 0/0/0 buffer size: 0 vbv_delay: N/A
frame=   32 fps=0.0 q=-1.0 size=      84KiB time=00:00:01.00 bitrate= 685.7kbits/s speed=   2x
frame=    0 fps=0.0 q=0.0 size=       0KiB time=N/A bitrate=N/A dup=0 drop=4 speed=N/A
frame=   47 fps= 47 q=-1.0 size=     110KiB time=00:00:01.50 bitrate= 600.3kbits/s speed= 1.5x
frame=    0 fps=0.0 q=0.0 size=       0KiB time=N/A bitrate=N/A dup=0 drop=4 speed=N/A
frame=   62 fps= 41 q=-1.0 size=     140KiB time=00:00:02.00 bitrate= 574.3kbits/s speed=1.33x
frame=    2 fps=1.3 q=29.0 size=       0KiB time=00:00:00.00 bitrate=N/A dup=0 drop=4 speed=   0x
frame=   77 fps= 38 q=-1.0 size=     169KiB time=00:00:02.50 bitrate= 553.9kbits/s speed=1.25x
frame=   17 fps=8.5 q=29.0 size=       0KiB time=00:00:00.50 bitrate=   0.8kbits/s dup=0 drop=4 speed=0.25x
frame=   92 fps= 37 q=-1.0 size=     206KiB time=00:00:03.00 bitrate= 560.7kbits/s speed= 1.2x
frame=   32 fps= 13 q=29.0 size=       0KiB time=00:00:01.00 bitrate=   0.4kbits/s dup=0 drop=4 speed= 0.4x
frame=  107 fps= 36 q=-1.0 size=     240KiB time=00:00:03.50 bitrate= 561.5kbits/s speed=1.17x
frame=   47 fps= 16 q=29.0 size=       0KiB time=00:00:01.50 bitrate=   0.3kbits/s dup=0 drop=4 speed= 0.5x
frame=  122 fps= 35 q=-1.0 size=     270KiB time=00:00:04.00 bitrate= 553.0kbits/s speed=1.14x
frame=   62 fps= 18 q=29.0 size=       0KiB time=00:00:02.00 bitrate=   0.2kbits/s dup=0 drop=4 speed=0.572x
frame=  137 fps= 34 q=-1.0 size=     299KiB time=00:00:04.50 bitrate= 543.7kbits/s speed=1.13x
frame=   77 fps= 19 q=29.0 size=       0KiB time=00:00:02.50 bitrate=   0.2kbits/s dup=0 drop=4 speed=0.625x
frame=  152 fps= 34 q=-1.0 size=     336KiB time=00:00:05.00 bitrate= 549.2kbits/s speed=1.11x
frame=   92 fps= 20 q=29.0 size=       0KiB time=00:00:03.00 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.667x
frame=  167 fps= 33 q=-1.0 size=     357KiB time=00:00:05.50 bitrate= 531.1kbits/s speed= 1.1x
frame=  107 fps= 21 q=29.0 size=       0KiB time=00:00:03.50 bitrate=   0.1kbits/s dup=0 drop=4 speed= 0.7x
frame=  182 fps= 33 q=-1.0 size=     394KiB time=00:00:06.00 bitrate= 537.1kbits/s speed=1.09x
frame=  122 fps= 22 q=29.0 size=       0KiB time=00:00:04.00 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.728x
frame=  197 fps= 33 q=-1.0 size=     426KiB time=00:00:06.50 bitrate= 536.4kbits/s speed=1.08x
frame=  137 fps= 23 q=29.0 size=       0KiB time=00:00:04.50 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.75x
frame=  212 fps= 33 q=-1.0 size=     452KiB time=00:00:07.00 bitrate= 528.8kbits/s speed=1.08x
frame=  152 fps= 23 q=29.0 size=       0KiB time=00:00:05.00 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.77x
frame=  227 fps= 32 q=-1.0 size=     479KiB time=00:00:07.50 bitrate= 522.8kbits/s speed=1.07x
frame=  167 fps= 24 q=29.0 size=       0KiB time=00:00:05.50 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.786x
frame=  242 fps= 32 q=-1.0 size=     508KiB time=00:00:08.00 bitrate= 519.3kbits/s speed=1.07x
frame=  182 fps= 24 q=29.0 size=       0KiB time=00:00:06.00 bitrate=   0.1kbits/s dup=0 drop=4 speed= 0.8x
frame=  257 fps= 32 q=-1.0 size=     553KiB time=00:00:08.50 bitrate= 532.5kbits/s speed=1.06x
frame=  197 fps= 25 q=29.0 size=       0KiB time=00:00:06.50 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.813x
frame=  272 fps= 32 q=-1.0 size=     584KiB time=00:00:09.00 bitrate= 531.1kbits/s speed=1.06x
frame=  212 fps= 25 q=29.0 size=       0KiB time=00:00:07.00 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.824x
frame=  287 fps= 32 q=-1.0 size=     610KiB time=00:00:09.50 bitrate= 525.7kbits/s speed=1.06x
frame=  227 fps= 25 q=29.0 size=       0KiB time=00:00:07.50 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.834x
[out#0/rtp @ 0x61de48332e00] video:622KiB audio:0KiB subtitle:0KiB other streams:0KiB global headers:2KiB muxing overhead: 1.105357%
frame=  300 fps= 32 q=-1.0 Lsize=     628KiB time=00:00:09.94 bitrate= 517.7kbits/s speed=1.06x
frame=  232 fps= 24 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.807x
frame=  232 fps= 23 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.767x
frame=  232 fps= 22 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.73x
frame=  232 fps= 21 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.697x
frame=  232 fps= 20 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.667x
frame=  232 fps= 19 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.639x
frame=  232 fps= 19 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.614x
frame=  232 fps= 18 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.59x
frame=  232 fps= 17 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.568x
frame=  232 fps= 17 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.548x
frame=  232 fps= 16 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.529x
frame=  232 fps= 15 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.511x
frame=  232 fps= 15 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.495x
frame=  232 fps= 14 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.479x
frame=  232 fps= 14 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.465x
frame=  232 fps= 14 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.451x
frame=  232 fps= 13 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.438x
frame=  232 fps= 13 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.426x
frame=  232 fps= 13 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.415x
frame=  232 fps= 12 q=29.0 size=       0KiB time=00:00:07.67 bitrate=   0.1kbits/s dup=0 drop=4 speed=0.404x
frame=  233 fps= 12 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.395x
frame=  233 fps= 12 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.385x
frame=  233 fps= 11 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.376x
frame=  233 fps= 11 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.367x
frame=  233 fps= 11 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.358x
frame=  233 fps= 11 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.35x
frame=  233 fps= 10 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.342x
frame=  233 fps= 10 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.335x
frame=  233 fps=9.9 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.328x
frame=  233 fps=9.7 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.321x
frame=  233 fps=9.5 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.314x
frame=  233 fps=9.3 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.308x
frame=  233 fps=9.1 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.302x
frame=  233 fps=9.0 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.296x
frame=  233 fps=8.8 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.291x
frame=  233 fps=8.6 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.285x
frame=  233 fps=8.5 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.28x
frame=  233 fps=8.3 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.275x
frame=  233 fps=8.2 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.27x
frame=  233 fps=8.0 q=29.0 size=       0KiB time=00:00:07.70 bitrate=   0.0kbits/s dup=0 drop=4 speed=0.266x
[in#0/sdp @ 0x58fa759468c0] Error during demuxing: Connection timed out
[out#0/mp4 @ 0x58fa75984380] video:266KiB audio:0KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: 1.627007%
frame=  296 fps= 10 q=-1.0 Lsize=     270KiB time=00:00:09.80 bitrate= 225.8kbits/s dup=0 drop=4 speed=0.335x
[libx264 @ 0x58fa7594ac80] frame I:2     Avg QP:21.26  size: 14844
[libx264 @ 0x58fa7594ac80] frame P:89    Avg QP:22.83  size:  1893
[libx264 @ 0x58fa7594ac80] frame B:205   Avg QP:28.72  size:   359
[libx264 @ 0x58fa7594ac80] consecutive B-frames:  4.4%  8.8%  3.0% 83.8%
[libx264 @ 0x58fa7594ac80] mb I  I16..4:  4.0% 52.5% 43.4%
[libx264 @ 0x58fa7594ac80] mb P  I16..4:  0.2%  1.5%  1.8%  P16..4: 18.5% 12.7%  9.2%  0.0%  0.0%    skip:56.1%
[libx264 @ 0x58fa7594ac80] mb B  I16..4:  0.0%  0.1%  0.1%  B16..8: 17.4%  3.2%  1.1%  direct: 0.6%  skip:77.5%  L0:33.9% L1:54.7% BI:11.5%
[libx264 @ 0x58fa7594ac80] 8x8 transform intra:46.1% inter:51.4%
[libx264 @ 0x58fa7594ac80] coded y,uvDC,uvAC intra: 85.8% 88.8% 63.2% inter: 6.4% 4.8% 1.1%
[libx264 @ 0x58fa7594ac80] i16 v,h,dc,p: 23% 53%  4% 19%
[libx264 @ 0x58fa7594ac80] i8 v,h,dc,ddl,ddr,vr,hd,vl,hu: 21% 19% 14%  5%  9%  8%  9%  7%  8%
[libx264 @ 0x58fa7594ac80] i4 v,h,dc,ddl,ddr,vr,hd,vl,hu: 27% 19% 12%  6%  8%  9%  7%  8%  5%
[libx264 @ 0x58fa7594ac80] i8c dc,h,v,p: 43% 25% 24%  8%
[libx264 @ 0x58fa7594ac80] Weighted P-Frames: Y:0.0% UV:0.0%
[libx264 @ 0x58fa7594ac80] ref P L0: 68.4% 14.5% 11.7%  5.3%
[libx264 @ 0x58fa7594ac80] ref B L0: 94.7%  4.2%  1.1%
[libx264 @ 0x58fa7594ac80] ref B L1: 96.6%  3.4%
[libx264 @ 0x58fa7594ac80] kb/s:220.09
MOCK_STREAM_DATA_STDERR

# Copy the sample_distorted file and rename it to the expected output of the network streaming script
cp "$1" "$2"
exit 0