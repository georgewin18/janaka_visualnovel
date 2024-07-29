label scene2:
    scene bg room
    with dissolve

    "Hari ini adalah hari yang istimewa bagiku. Aku akan mengambil almamater PENS, jubah abu-abu yang akan menjadi tanda kebanggaanku sebagai mahasiswa baru."

    "Setelah mandi dan sarapan cepat, aku melangkah keluar rumah menuju perjalanan yang akan mengubah statusku menjadi mahasiswa PENS."

    "Langkahku mantap saat aku meninggalkan rumah menuju kampus."

    scene bg d3
    with dissolve

    show raden idle with dissolve

    "Begitu tiba di sana, suasana ramai dan penuh semangat menyambutku. Para mahasiswa baru seperti aku diminta untuk mengantre untuk registrasi. Meskipun antriannya cukup panjang, para panitia terlihat sangat terorganisir sehingga situasinya tetap terkendali."

    "Beberapa di antaranya tampak santai sambil bercanda dengan teman-teman baru mereka."

    show raden idle with moveinleft:
        xalign 0.75

    "Aku berada dalam antrian untuk mengambil almamater, sambil tetap memperhatikan sekitar. Di sebelahku, beberapa wajah baru dengan ekspresi campuran antara gugup dan antusiasme terlihat menunggu giliran mereka."

    stop music fadeout 2.0
    
    show anon_chara with moveinleft:
        xalign 0.25

    voice "audio/vo/aisyah/duh.mp3"
    anon "\"Duh, ini antrinya lama banget sih,\""

    voice sustain
    "Aku menoleh ke belakang dan melihat seorang cewek polos menggunakan kerudung. Ekspresi wajahnya memperlihatkan sedikit kekesalan akibat menunggu terlalu lama."

    hide anon_chara with dissolve
    show aisyah grump with dissolve:
        xalign 0.25

    play music aisyah_bgm volume 0.5 fadein 1.0

    voice "audio/vo/aisyah/sampaikapan.mp3"
    anon "Sampai kapan ini antriannya?"

    voice sustain
    "Dia mengenakan yang terlihat sederhana namun rapi. Tatapan matanya mencari-cari jawaban dari siapa pun yang bisa memberikan informasi tentang kecepatan proses antrian ini."

    show raden happy

    "Aku tersenyum ramah padanya, mencoba meredakan sedikit kekecewaannya."

    r "Kurang tahu sih, haruse bentar lagi juga jalan"

    show aisyah happy

    voice "audio/vo/aisyah/hah.mp3"
    a "Ya, semoga saja,"

    voice sustain
    a "Ngomong-ngomong, kamu dari jurusan apa?"

    r "Aku dari Departeman Mekanika, kamu?"

    voice "audio/vo/aisyah/hai.mp3"
    a "Teknik Informatika, Namaku Aisyah, by the way."

    voice sustain
    r "Aku Raden, Salam kenal."

    "Kami berbincang ringan selama antrian bergerak maju. Aisyah tampak lebih santai setelah beberapa saat, dan percakapan kami membuat waktu terasa lebih cepat. Akhirnya, tibalah giliranku di meja registrasi."

    p "Halo, atas nama..? Departemen?"

    r "Raden, Mekanika"

    "Setelah menerima almamater, aku melangkah sedikit ke samping untuk memberi ruang bagi Aisyah.. Dia terlihat senang ketika akhirnya tiba gilirannya. Sambil menunggu, aku membolak-balik almamater yang masih terlipat di dalam plastik."

    voice "audio/vo/aisyah/mencoba.mp3"
    a "Tidak ingin mencoba?"

    voice sustain
    r "Di rumah saja, aku malas ngelipat lagi."

    voice "audio/vo/aisyah/okcoba.mp3"
    a "Oke, aku mau coba, lihatin cocok apa enggak?"

    voice sustain
    "Aisyah segera membuka plastik dan mengeluarkan almamaternya. Dengan hati-hati, dia mengenakan jubah abu-abu tersebuti. Aku mengamatinya dengan seksama."

    scene bg aisyah_almamater
    with dissolve

    "Penampilannya tampak memukau di mataku. Kerudung pastel yang ia kenakan kontras dengan warna abu-abu jubah almamater, memberikan kesan yang anggun dan elegan. Almamater itu terlihat pas di tubuhnya, membuatnya tampak lebih percaya diri."

    "Matanya yang besar dan ekspresif bersinar dengan kegembiraan saat ia berputar perlahan, menunjukkan bagaimana almamater itu membalut tubuhnya dengan sempurna."

    "Senyum hangatnya membuat seluruh penampilannya semakin memikat, dan pipinya yang sedikit merona menambah keindahan alami wajahnya."

    "Blus putih dengan hiasan renda yang ia kenakan sebelumnya kini tersembunyi di balik almamater, namun rok panjang berwarna navy yang menjuntai tetap terlihat, memberikan sentuhan kesederhanaan yang menawan."

    "Sepatu flat hitamnya yang sederhana namun elegan melengkapi penampilan keseluruhan."

    scene bg d3

    show aisyah vhappy:
        xalign 0.25
    show raden happy:
        xalign 0.75
    with dissolve

    voice "audio/vo/aisyah/gimana.mp3"
    a "Bagaimana? Cocok nggak?"

    voice sustain
    r "Cocok banget. Kamu kelihatan keren."

    show aisyah shy

    voice "audio/vo/aisyah/makasi.mp3"
    a "Haha, makasih."

    voice sustain
    show aisyah vhappy

    r "Aku cuma jujur, kok,"

    r "Almamater itu benar-benar pas di kamu."

    voice "audio/vo/aisyah/pakaijas.mp3"
    a "Memakai jas kek gini membuatku seperti orang dewasa."

    voice sustain
    r "Memang sudah waktunya dewasa,"

    "Aisyah tertawa, dan suara tawanya lembut serta menenangkan. Bahunya sedikit naik turun saat dia tertawa, dan matanya menyipit, memperlihatkan kerutan kecil di sudut-sudutnya. Ada keanggunan alami dalam cara dia tertawa, memperlihatkan senyumnya yang lebar dan hangat."

    r "Enggak foto? Sini tak fotoin dah,"

    show aisyah happy

    voice "audio/vo/aisyah/gasuka.mp3"
    a "Gak mau, gak suka foto-foto aku,"

    voice sustain
    r "Yah, sayang banget. Padahal momen ini harus diabadikan,"

    "Kami melanjutkan obrolan sambil berjalan menuju gerbang kampus. Topik pembicaraan bergeser ke mata kuliah yang akan kami ambil, dosen-dosen terkenal, dan kegiatan ekstrakurikuler yang menarik."

    stop music fadeout 2.0

    show aisyah nervous

    "Namun, tiba-tiba Aisyah tampak termenung. Matanya melamun sejenak, seperti ada sesuatu yang membebani pikirannya."

    show raden idle

    r "Kamu kenapa?"

    voice "audio/vo/aisyah/gpp.mp3"
    a "Oh, enggak apa-apa. Cuma kepikiran aja,"

    voice sustain
    "Aku merasa ada sesuatu yang dia sembunyikan, tapi memutuskan untuk tidak mendesaknya. Maksudku, semua orang memiliki masalah sendiri bukan?"

    r "Oke, Aisyah. Sampai jumpa besok, ya,"

    voice "audio/vo/aisyah/sampaijumpa.mp3"
    a "Sampai jumpa, Raden. Terima kasih untuk hari ini,"

    voice sustain
    jump scene3

    return