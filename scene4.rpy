label scene4:
    scene bg parkiran
    with dissolve

    show raden idle with moveinleft

    "Pagi itu, udara masih terasa sejuk saat aku tiba di depan parkir gedung D3 PENS. Jam di tanganku menunjukkan pukul 05.45, lima belas menit lebih awal dari waktu yang ditentukan. Aku sengaja datang lebih awal agar tidak terburu-buru dan bisa mengamati suasana sekitar."

    "Hari ini adalah hari pertama aku resmi menjadi mahasiswa baru PENS. Meski sedikit bersemangat, aku selalu berpikir PKKMB adalah hal yang membosankan. Materi-materi yang gak jelas, apalagi tugas yang diberikan kakak tingkat pasti gak guna banget."

    "Memang banyak kasus senioritas seperti itu. Bahkan sering tersebar juga ke media sosial dan dibahas juga oleh para influencer."

    "Tetapi untungnya maba PENS tidak disuruh menggunakan yang aneh-aneh seperti penutup kepala yang dipasangi balon, kalung nametag dengan hiasan konyol, atau teka-teki snack yang benar-benar gak guna."

    "Mataku menyapu halaman parkir yang sudah dipenuhi oleh ratusan mahasiswa baru. \"Wow, maba PENS ternyata banyak juga,\" gumamku dalam hati. Aku merasa sedikit gugup melihat begitu banyak wajah baru yang asing bagiku."

    "Secara tidak sadar, aku mulai mencari-cari sosok Aisyah di antara kerumunan mahasiswa baru. Dia adalah satu-satunya orang yang kukenal di kampus ini. Setidaknya, jika aku bisa menemukannya, aku tidak akan merasa terlalu sendirian."

    "Aku berjalan perlahan menyusuri kerumunan, mataku terus mencari-cari sosok Aisyah. Namun, hingga beberapa menit kemudian, aku masih belum menemukannya."

    r "Mungkin dia belum datang,"

    stop music fadeout 2.0

    p "{size=+10}Bagi para peserta silakan berbaris sesuai dengan departemennya masing-masing untuk melakukan registrasi!{/size}"

    show raden idle with moveinleft:
        xalign 0.75
    show anon_chara with MoveTransition(0.3, enter=offscreenleft):
        xalign 0.55
    
    play sound "audio/sfx/bump.mp3"
    "{size=+10}!!{/size}" with hpunch

    show anon_chara with moveinright:
        xalign 0.25

    voice "audio/vo/fania/aduh.mp3"
    anon "Aduh-aduh, maaf ya, aku kira aku telat!"

    voice sustain
    play music raden_bgm volume 0.5 fadein 1.0

    hide anon_chara with dissolve
    show fania panic with dissolve:
        xalign 0.25
    
    "Aku menoleh dan melihat seorang perempuan dengan rambut panjang yang diikat, wajahnya terlihat cemas."

    r "Ah, iya-iya, gpp, santai aja,"

    r "Hati-hati lah, Mbak, nanti kalau jatuh bisa bikin geger satu PENS."

    show fania happy

    voice "audio/vo/fania/hehe.mp3"
    f "Hehe, kukira aku telat,"

    voice sustain
    show raden idle at right with moveinleft
    show fania happy at center with moveinleft
    show panitia at left with moveinleft

    p "Departemen apa, Mbak?"

    voice "audio/vo/fania/dtmk.mp3"
    f "DTMK,"

    voice sustain
    p "Oh, DTMK sebelah situ, Mbak,"

    "Perempuan itu mengangguk, lalu berlari kecil menuju barisan yang ditunjukkan oleh panitia. Aku hanya bisa menggelengkan kepala sambil tersenyum."   

    hide panitia
    hide fania 
    with moveoutleft
    hide raden with moveoutright

    scene bg gedung_tc
    with slideawayleft

    show raden idle with moveinleft

    "Meja registrasi akhirnya di depan mata. Aku menyerahkan berkas-berkas yang diminta, lalu mulai mengisi formulir. Nama, cek. Jam registrasi, cek. Tapi, saat tiba di kolom NRP, otakku mendadak blank."

    "\"NRP-ku berapa ya?\" gumamku sambil menggaruk kepala. Aku mencoba mengingat-ingat, tapi nihil. Rasanya semua angka bercampur aduk di kepalaku."

    "\"Duh, kok lupa sih?\" Aku mulai panik, keringat dingin mulai mengucur di dahiku. Aku melirik ke belakang, antrian sudah mulai mengular. Tiba-tiba aku teringat sesuatu,"

    "Eh, tunggu dulu! Kan ada di kartu pesertaku!"

    p "{size=+10}Jalannya dipercepat teman-teman, sapa seluruh warga PENS!{/size}" with hpunch

    "\"Gilak, nggak capek apa ngomong gitu terus?\" pikirku sambil berjalan menuju gedung Pascasarjana."

    hide raden with moveoutleft

    scene bg gedung_ps
    with slideawayright

    show raden idle with moveinleft

    "Namun, saat sampai di gedung, aku tercengang. Ternyata, kami harus naik tangga sampai ke {size=+10}lantai 6!{/size}"

    r "{size=+10}Woila, cik, yang bener ini naik lantai 6?{/size}" with hpunch

    "Aku mulai menaiki tangga dengan langkah gontai. Baru beberapa anak tangga, aku hampir saja kepleset karena lantai tangganya yang agak licin."

    r "Aduh, hampir aja jadi tontonan gratis nih,"

    scene bg depan_audit
    with slideawaydown

    "Akhirnya, setelah perjuangan yang cukup melelahkan, aku berhasil sampai di lantai 6. Aku mengatur napasku sambil menyeka keringat di dahi."

    jump scene5

    return