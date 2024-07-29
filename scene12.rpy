label scene12:
    scene bg depan_audit
    with dissolve

    "Keesokan harinya, kami semua diminta untuk berkumpul dengan masing-masing kelompok, kelompok kami dipandu menuju Selasar lt 5."

    "Kami diberitahu bahwa akan ada sesi debat tentang kearifan lokal. Setiap kelompok diminta untuk membagi diri menjadi dua tim: tim pro dan tim kontra. Aku dan teman-teman kelompokku segera berdiskusi dan menentukan posisi masing-masing."

    show sekar happy with dissolve

    voice "audio/vo/sekar/pagi.mp3"
    s "Selamat pagi semuanya,"

    voice sustain
    s "Jadi hari ini kita akan mengadakan sesi debat tentang kearifan lokal. Setiap kelompok harus membagi diri menjadi dua tim, tim pro dan tim kontra. Silakan diskusikan di antara kalian dan tentukan siapa yang akan berada di tim mana ya."

    show sekar happy at left with moveinleft
    show anon_chara at right with dissolve
    show raden idle with dissolve
    
    anon "Raden, kamu yakin mau di tim pro?"

    r "Iya, gue yakin. Gue punya beberapa argumen kuat tentang pentingnya kearifan lokal,"

    anon "Semoga argumen kamu kuat ya, Raden. Siap-siap kalah sama tim kita,"

    r "Kita lihat aja nanti."

    play sound "audio/sfx/crowd_talking.mp3" fadein 1.0 volume 0.5 loop
    "Debat pun dimulai. Tim pro memulai dengan argumen-argumen tentang pentingnya mempertahankan kearifan lokal dalam budaya modern."

    "Kami berbicara tentang bagaimana kearifan lokal dapat menjadi identitas dan kekuatan bangsa, serta bagaimana nilai-nilai yang terkandung di dalamnya masih relevan hingga saat ini."

    "Selama debat berlangsung, mataku tidak bisa melihat ke arah lain selain pemandu kami, Kak Sekar. Dia tampak kelelahan, matanya terlihat seperti mengantuk dan lelah, namun seolah mencoba menutupi itu di depan adik kelasnya."

    "Aku bisa melihat dari gerak-geriknya bahwa dia benar-benar berusaha keras untuk tetap tampil profesional dan bersemangat."

    "Kak Sekar sesekali memberikan komentar dan pertanyaan yang membuat kami berpikir lebih kritis."

    voice "audio/vo/sekar/hmmbaik.mp3"
    s "Baik, argumen kalian sangat menarik. Sekarang, mari kita dengarkan tanggapan dari tim pro."

    stop sound fadeout 2.0
    "Akhirnya, setelah beberapa waktu, debat pun usai. Kak Sekar memberikan apresiasi kepada semua peserta."

    hide anon_chara with dissolve
    show raden idle with moveinleft:
        xalign 0.75
    show sekar happy with moveinleft:
        xalign 0.25

    s "Terima kasih atas partisipasi kalian. Debat ini bukan tentang siapa yang menang atau kalah, tapi tentang bagaimana kita bisa belajar dan menghargai perspektif yang berbeda."

    "Kami diminta untuk menunggu arahan selanjutnya. Aku mencoba mencairkan suasana dengan mengajak berbicara Kak Sekar."

    r "Kak, Kak Sekar jadi panitia buat apa? Kan kalau liburan gini enakan tidur di rumah,"

    s "Oh jangan panggil kak, mbak aja. Di PENS itu kebiasaannya pakai mas atau mbak. Banyak loh alasan buat ikut kepanitiaan, bisa dapet relasi, pengalaman organisasi, dan masih banyak lagi. Kenapa? Pengen ikut ya?"

    show raden happy

    r "Mungkin nanti, mbak. Tapi serius, kelihatan capek banget. Ngurusin kita semua pasti nggak gampang."

    show sekar nervous

    voice "audio/vo/sekar/iyalah.mp3"
    s "Iya, memang capek, tapi senang juga. Melihat kalian semua semangat dan antusias."

    voice sustain
    show raden nervous

    r "Tapi loh..,"

    show sekar happy

    voice "audio/vo/sekar/gakpapa.mp3"
    s "Enggak papa kok, capek dikit soalnya kemarin aku setelah acara kerja dulu. Tapi nggak papa, kalau lihat kalian semangat, aku juga semangat."

    voice sustain
    show raden idle

    r "Wah, kak, hebat banget masih bisa semangat. Kami jadi termotivasi juga loh."

    voice "audio/vo/sekar/begitulah.mp3"
    s "Ya begitulah, kadang capek, tapi kalau kita lakukan dengan hati, semua terasa lebih ringan, toh kalau ikut kegiatan kan itu tanggung jawab kita juga."

    voice sustain
    "Setelah itu kami diminta untuk kembali ke auditorium untuk melanjutkan acara Technogear"

    jump scene13

    return