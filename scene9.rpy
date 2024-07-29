label scene9:
    scene bg d3 
    with dissolve

    "Matahari yang mulai terbenam memberikan cahaya oranye lembut di langit, menambah kehangatan suasana."

    "Saat sedang kembali ke tempat dudukku aku melihat seorang perempuan yang menabrakku sedang berbicara dengan beberapa mahasiswa baru, dia tampak seperti seseorang yang {i}friendly{/i}"
    
    r "Pasti tu orang bakal punya banyak temen sih fix"

    "Sore semakin merambat malam, dan langit mulai beralih dari oranye lembut ke warna biru gelap. Terdengar suara dari pengeras suara yang digunakan oleh panitia acara."

    p "{size=+10}Perhatian seluruhnya! Kami mohon kepada semua peserta untuk segera berkumpul dan bersiap-siap untuk pulang.{/size}"

    stop music fadeout 2.0

    "Saat sedang mengantre, aku melihat perempuan itu berada di sebelahku."

    play music fania_bgm volume 0.3 fadein 1.0

    show fania idle:
        xalign 0.25
    show raden idle:
        xalign 0.75
    with dissolve

    r "Eh, kamu.. yang itu kan..?,"

    show fania nervous

    voice "audio/vo/fania/heheiya.mp3"
    f "Hehe, iya... Btw, maaf ya soal kemarin, nggak sengaja soalnya. Sumpah,"

    voice sustain
    f "Oh iya, aku Fania. Kamu?"

    r "Raden. Keren sih tadi, aku sempat ngelihat kamu sekilas. Ngobrolnya kelihatan asik banget."

    show fania happy

    voice "audio/vo/fania/hehehe.mp3"
    f "Muehehe... Ya biasalah, cari teman. Waktu kuliah ya perbanyak koneksi lah,"

    voice sustain
    show raden happy

    r "Bener juga. Btw kek dejavu ya, kita pertama kali ketemu waktu registrasi eh ketemu lagi pas registrasi."

    show fania vhappy

    voice "audio/vo/fania/hehe.mp3"
    f "Iya ya haha"

    voice sustain
    "Dilihat bagagimanapun dia adalah tipe yang gampang dikenali oleh siapapun."

    show fania happy

    voice "audio/vo/fania/duluan.mp3"
    f "Duluan ya Raden, sampai ketemu besok ya?"

    voice sustain
    r "Sampai ketemu besok, Fania."

    hide fania with moveoutleft
    show raden idle at center with moveinright

    "Kami saling melambaikan tangan sebelum akhirnya berjalan menuju arah masing-masing. Fania tampak mengisi formulir presensi dan segera pergi ke arah parkiran. Namun, antrean untuk DTME masih sangat panjang."

    stop music fadeout 2.0

    r "Woila ini lama amat kenapa weh , gweh pengen muleh ini"

    play music raden_bgm volume 0.5 fadein 1.0

    anon "Tau ni, harus sabar kek gimana lagi nih, dah laper."

    r "Rill cuy, udah mah lapar, ngantuk pula."

    show raden idle with moveinright:
        xalign 0.25
    show sekar happy with moveinright:
        xalign 0.75

    voice "audio/vo/sekar/sabarlah.mp3"
    p "Iya sabar, kan yang mau presensi gak kamu aja"

    p "Kamu dari departemen mana?"

    r "DTME kak"

    p "Oh. Ini DTMK, DTME sebelah situ, yang udh selesai duluan"

    show raden shock

    r "{size=+10}ALAMAKKK{/size}" with vpunch

    r "Harusnya udah pulang dari tadi aku, terima kasih kak"

    show sekar vhappy

    "\"Yang lucu apa dah, kok ketawa?\" tanyaku didalam hati"

    jump scene10

    return