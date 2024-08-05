# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Raden")
define a = Character("Aisyah")
define f = Character("Fania")
define s = Character("Sekar")
define d = Character("Dheo")
define p = Character("Panitia")
define anon = Character("...")

define audio.raden_bgm = "audio/bgm/raden.flac"
define audio.main_bgm = "audio/bgm/main_menu.flac"
define audio.aisyah_bgm = "audio/bgm/aisyah_sweet.flac"
define audio.fania_bgm = "audio/bgm/fania_energic.flac"
define audio.sekar_bgm = "audio/bgm/sekar.flac"
define audio.sad_bgm = "audio/bgm/sad.flac"
define audio.dheo_bgm = "audio/bgm/dheo.flac"
define audio.end_bgm = "audio/bgm/ed.flac"
define config.default_voice_volume = 0.8

define silhouette = Matrix([0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 1.0])

image splash = "splash/logo.png"
image blank = "splash/blank.png"

label splashscreen:
    scene blank with Pause(1)

    show splash with dissolve:
        zoom 0.4 truecenter
    with Pause(2)
    
    scene blank with dissolve 
    with Pause(1)

    return

label start:
    stop music fadeout 2.0

    scene bg start with dissolve
    with Pause(2)

    play music raden_bgm volume 0.5 fadein 1.0

    scene bg kamar with dissolve:
        yzoom 1.01

    "Aku duduk di meja belajarku, jemariku menari di atas keyboard laptop. Cahaya layar monitor menerangi wajahku, menciptakan bayangan di sudut-sudut ruangan yang sepi."

    r "Halo, namaku Raden. Baru-baru ini aku menjadi mahasiswa di PENS, Politeknik Elektronika Negeri Surabaya."

    r "Awalnya, aku bermimpi bisa kuliah bersama pacarku, tetapi hubungan kami berakhir sebelum kuliah dimulai."

    r "Sejujurnya, aku berniat ingin bekerja, tapi teman-teman meyakinkanku untuk mencoba SNBT di PENS. Katanya sih salah satu universitas top di Surabaya. Tapi, aku hanya tahu ITS tidak pernah mendengar ada kampus PENS."

    show bg laptop with dissolve

    play sound "audio/sfx/typing_short.mp3" volume 0.3
    r "Aku mencoba mencari kata PENS di internet dan yang muncul malah.."

    r "{size=+10}PULPEN?!{/size} apasih? kok malah gambar jualan pulpen" with vpunch

    r "Di bagian bawah hasil pencarian tersebut, memang ada juga kampus PENS. Meskipun demikian, terasa sedikit aneh bahwa yang paling atas adalah gambar-gambar pulpen, bukan langsung mengenai kampus PENS."

    r "Aku mencoba mencari tahu lebih lanjut mengenai kampus. Tentu saja yang aku cek pertamakali adalah biaya UKT yang ternyata begitu murah, bahkan ada juga opsi beasiswa. Kemudian aku mengecek Fasilitas, partnership, lingkungan dan lain-lain."

    r "Setelah beberapa pertimbangan, aku berpikir bahwa tidak ada salahnya mencoba."

    "{i}nothing to lose{/i}"

    scene bg kamar with dissolve:
        yzoom 1.01

    r "Dengan perlahan, aku menutup laptop."

    r "Kemudian, aku mulai menyiapkan peralatan untuk PKKMB besok. Tas ransel kuat yang telah aku siapkan semalam sudah kugantungkan di sandaran kursi. Almamater abu-abu PENS terlipat rapi di atas meja, bersama dengan buku catatan dan pena."
    
    r "Aku memeriksa satu per satu, memastikan semua sudah siap untuk hari besar ini."

    r "Aku tersenyum, menatap langit-langit, penuh harapan bahwa semuanya akan baik-baik saja."

    "{i}Semoga...{/i}"

    jump scene2

    return
