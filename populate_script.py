import sqlite3

conn = sqlite3.connect("votes.db")
cur = conn.cursor()

# Add subjects
subjects = [
    "Ona tili va adabiyot",
    "Rus tili (milliy)",
    "Ingliz tili",
    "Matematika",
    "Fizika",
    "Kimyo",
    "Informatika",
    "Geografiya",
    "Biologiya",
    "Tarix",
    "Davlat va huquq asoslari",
    "Tarbiya",
    "Boshlang'ich ta'lim",
    "Musiqa madaniyati",
    "Texnologiya",
    "Jismoniy tarbiya",
    "Tasviriy san'at va chizmachilik",
    "CHQBT"
]

for name in subjects:
    cur.execute("INSERT OR IGNORE INTO subjects (name) VALUES (?)", (name,))
conn.commit()

# Get subject IDs
cur.execute("SELECT id, name FROM subjects")
subject_map = {name: id for id, name in cur.fetchall()}

# Add teachers
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Matrizayeva Nigora Ruzmatovna", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Jumaniyozova Nilufar Davronbek kizi", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Bobojanova Dinora Rashidovna", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Axmedova Xurshida Farxodovna", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Ollazarova Adolat Ochilovna", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Kurbonova Dilrabo Jumaboevna", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Rajabova Charos Sultonboyevna", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Azizova Yulduz Shonazarovna", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Qolandarova Moxira Yashinbayevna", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Ruzmetova Go'zal Baxodirovna", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Jumabayeva Anajon Odilbek qizi", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Rizayeva Gulnoza Otabekovna", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Quziyeva Sug'diyona Ilxam qizi", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Raximova Gulzoda Zafar qizi", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Matyaqubova Muqaddas Abdusharip qizi", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Raxmanova Miyassar Yuldashevna", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Abdrimova Liliya Rajabovna", subject_map["Boshlang'ich ta'lim"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Mahmudova Nargiza Rustamovna", subject_map["Ona tili va adabiyot"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Davletova Shaxzoda Arslonbekovna", subject_map["Ona tili va adabiyot"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Musajonova Shahzoda Muxamedovna", subject_map["Ona tili va adabiyot"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Aminova Munisxon Hamdamjonovna", subject_map["Ona tili va adabiyot"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Shavkatov Bexroz Alisher o'g'li", subject_map["Ona tili va adabiyot"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Sadullayeva Matluba Bahodir qizi", subject_map["Ona tili va adabiyot"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Djabbarova Nodira Xayrullaevna", subject_map["Rus tili (milliy)"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Razzakova Zulayxo Karimboy qizi", subject_map["Rus tili (milliy)"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("G'aniyeva Moxira G'ayrat qizi", subject_map["Rus tili (milliy)"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Bardiyeva Parizoda Sherzod qizi", subject_map["Rus tili (milliy)"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Umirova Umida Zokirovna", subject_map["Rus tili (milliy)"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Boltaeva Ayshajon Rustamovna", subject_map["Ingliz tili"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Bobojonova Maxfuza Uktamboevna", subject_map["Ingliz tili"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Raximova Maksuda Ilxambekovna", subject_map["Ingliz tili"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Yo'ldasheva Maftuna Ravshanbek qizi", subject_map["Ingliz tili"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Gaipnazarova Dilafruz Rustam qizi", subject_map["Ingliz tili"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Madaminova Irina Aleksandrovna", subject_map["Ingliz tili"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Durumbayeva Sevaraxon G'ayrat qizi", subject_map["Ingliz tili"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Matyaqubova Gulnoza Ozadboy qizi", subject_map["Ingliz tili"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Begnazarova Lolaxon Madsudbek qizi", subject_map["Ingliz tili"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Matkarimova Xulkar Anvarovna", subject_map["Ingliz tili"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Matkarimova Surayyo Mirzayevna", subject_map["Matematika"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Abdrimova Gulmira Azamatovna", subject_map["Matematika"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Raximova Sarvinoz Adilbekovna", subject_map["Matematika"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Rayimov Doniyor Davronboevich", subject_map["Matematika"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Raxmanova Dilnoza Xudaynazarovna", subject_map["Matematika"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Klicheva Ma'mura Xaitboevna", subject_map["Matematika"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Boltaev Sarvarbek Ravshanbekovich", subject_map["Informatika"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Matqurbonov Behruzbek Maqsud o'g'li", subject_map["Informatika"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Ollaberganova Malika Bobojan qizi", subject_map["Geografiya"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Masharipova Munojot Zoxirovna", subject_map["Fizika"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Matkulieva Nodira Yuldashevna", subject_map["Kimyo"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Saydimova Muxayyo Narmatovna", subject_map["Biologiya"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Kamalova Hurmatoy Hamroyevna", subject_map["Biologiya"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Xodjayeva Barno Ibragimovna", subject_map["Texnologiya"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Xalilova Fotima Xalillayevna", subject_map["Texnologiya"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Xajiyeva Dinara Po'latovna", subject_map["Texnologiya"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Matkarimova Sharifa Shuxratovna", subject_map["Texnologiya"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Duschanova Yorkinoy Erkinboyevna", subject_map["Musiqa madaniyati"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Boltayeva Go'zalxon Maqsudbekovna", subject_map["Musiqa madaniyati"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Baltabayeva Shaxnoza Xayitboy qizi", subject_map["Tasviriy san'at va chizmachilik"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Ruziyeva Fotima Seyitmamatona", subject_map["Tasviriy san'at va chizmachilik"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Yuldosheva Nilufar Davronbekovna", subject_map["Tarix"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Yuldoshova Salomatxon Tajimbaevna", subject_map["Tarix"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Xajiyeva Farida Shermat qizi", subject_map["Davlat va huquq asoslari"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Bekchanova Go'zal To'lqinovna", subject_map["Tarix"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Rajabbayev Azizbek Kaxromonovich", subject_map["Jismoniy tarbiya"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Sodiqova Barno Xo'janazarqizi", subject_map["Jismoniy tarbiya"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Xudoynazarova Kuvonchoy Farxodovna", subject_map["Jismoniy tarbiya"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Matyaqubov Azamat Omongeldiyevich", subject_map["Jismoniy tarbiya"]))
cur.execute("insert into teachers (name, subject_id) values (?, ?)", ("Avazmatov Shoxrux Odilbekovich", subject_map["Jismoniy tarbiya"]))

conn.commit()
conn.close()
