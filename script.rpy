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
define audio.sad_bgm = "audio/bgm/sad.flac"
define config.default_voice_volume = 0.8

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    stop music fadeout 0.5
    play music raden_bgm volume 0.5 fadein 1.0

    scene bg room

    "Aku duduk di meja belajarku, jemariku menari di atas keyboard laptop. Cahaya layar monitor menerangi wajahku, menciptakan bayangan di sudut-sudut ruangan yang sepi."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show raden happy with dissolve

    # These display lines of dialogue.

    r "Halo, namaku Raden. Baru-baru ini aku menjadi mahasiswa di PENS, Politeknik Elektronika Negeri Surabaya."

    show raden sad

    r "Awalnya, aku bermimpi bisa kuliah bersama pacarku, tetapi hubungan kami berakhir sebelum kuliah dimulai."

    show raden idle

    r "Sejujurnya, aku berniat ingin bekerja, tapi teman-teman meyakinkanku untuk mencoba SNBT di PENS. Katanya sih salah satu universitas top di Surabaya. Tapi, aku hanya tahu ITS tidak pernah mendengar ada kampus PENS."

    play sound "audio/sfx/typing_short.mp3" volume 0.3
    r "Aku mencoba mencari kata PENS di internet dan yang muncul malah.."

    r "{size=+10}PULPEN?!{/size} apasih? kok malah gambar jualan pulpen" with vpunch

    r "Di bagian bawah hasil pencarian tersebut, memang ada juga kampus PENS. Meskipun demikian, terasa sedikit aneh bahwa yang paling atas adalah gambar-gambar pulpen, bukan langsung mengenai kampus PENS."

    r "Aku mencoba mencari tahu lebih lanjut mengenai kampus. Tentu saja yang aku cek pertamakali adalah biaya UKT yang ternyata begitu murah, bahkan ada juga opsi beasiswa. Kemudian aku mengecek Fasilitas, partnership, lingkungan dan lain-lain."

    r "Setelah beberapa pertimbangan, aku berpikir bahwa tidak ada salahnya mencoba."

    "{i}nothing to lose{/i}"

    r "Dengan perlahan, aku menutup laptop."

    r "Kemudian, aku mulai menyiapkan peralatan untuk PKKMB besok. Tas ransel kuat yang telah aku siapkan semalam sudah kugantungkan di sandaran kursi. Almamater abu-abu PENS terlipat rapi di atas meja, bersama dengan buku catatan dan pena."
    
    r "Aku memeriksa satu per satu, memastikan semua sudah siap untuk hari besar ini."

    r "Aku tersenyum, menatap langit-langit, penuh harapan bahwa semuanya akan baik-baik saja."

    hide raden with dissolve

    "{i}Semoga...{/i}"

    jump scene2

    # This ends the game.

    return
