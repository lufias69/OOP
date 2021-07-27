#!/usr/bin/env python
# coding: utf-8

# <h1 class="f1 mv1">Python: Access Modifiers (Atau Enkapsulasi)</h1>
# <img src="img/cover.webp" alt=" " width="300" height="600" align="left"/>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# Access Modifiers adalah sebuah konsep di dalam pemrograman berorientasi objek <br>dimana kita bisa mengatur hak akses suatu atribut dan fungsi pada sebuah class. <br>Konsep ini juga biasa disebut sebagai enkapsulasi, <br>di mana kita akan mendefinisikan mana atribut atau fungsi yang boleh diakses secara terbuka, <br>mana yang bisa diakses secara terbatas, atau mana yang hanya bisa diakses oleh internal kelas alias privat.
# <h2 id="jenis-access-modifiers-pada-python">Jenis Access Modifiers Pada Python</h2>
# <p>Sama seperti bahasa pemrograman berbasis objek lainnya  
#     <br>semisal java, c++, php, dan lain-lain, <br>python juga mendukung fitur access modifiers.</p>
# <p>Access modifiers yang tersedia di dalam python ada 3:</p>
# <ol>
# <li>Public</li>
# <li>Protected</li>
# <li>dan Private</li>
# </ol>
# <p>&nbsp;</p>
# <img src="img/enkapsulasi.svg" alt=" " width="400" height="800" align="left"/>
# 
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <h2 >Public Access Modifier</h2>
# <p>Variabel atau atribut yang memiliki hak akses publik bisa diakses dari mana saja <br>baik dari luar kelas mau pun dari dalam kelas.</p>
# <p>Perhatikan contoh berikut:</p>
# </div>

# In[1]:


class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi 


# Pada contoh di atas, kita membuat sebuah kelas dengan nama Segitiga. <br>Kelas tersebut menerima dua buah parameter: yaitu alas dan tinggi.
# <br>Kemudian ia juga memiliki 3 buah atribut (alas, tinggi, dan luas) <br>yang mana semuanya memiliki hak akses publik.
# <br>Untuk membuktikannya, mari kita coba akses ke-3 atribut di atas dari luar kelas:

# In[ ]:





# In[2]:


segitiga_besar = Segitiga(100, 80)
# akses variabel alas, tinggi, dan luas dari luar kelas
print('alas:', segitiga_besar.alas)
print('tinggi:', segitiga_besar.tinggi)
print('luas:', segitiga_besar.luas)


# <h2 >Protected Access Modifier</h2>
# Variabel atau atribut yang memiliki hak akses protected <br>hanya bisa diakses secara terbatas oleh dirinya sendiri (yaitu di dalam internal kelas), <br>dan juga dari kelas turunannya.
# <p>Mari kita mencoba mempraktikkannya.</p>
# <p>Untuk mendefinisikan atribut dengan hak akses&nbsp;<em>protected</em>, kita&nbsp;<strong>harus</strong>&nbsp;menggunakan prefix underscore&nbsp;<code>_</code>&nbsp;sebelum nama variabel.</p>

# In[37]:


class Mobil:
    def __init__(self, merk):
        self._merk = merk


# Pada kode program di atas, kita membuat sebuah kelas bernama <font color="red">Mobil</font>. <br>Dan di dalam kelas tersebut, kita mendefinisikan satu buah atribut bernama <font color="red">_merk</font>, <br>yang mana hak akses dari atribut tersebut adalah protected karena nama variabelnya diawali oleh underscore (<font color="red">_</font>).
# 
# Mari kita coba akses dari luar kelas:

# In[9]:


sedan = Mobil('Toyota')

# tampilkan _merk dari luar kelas
print('Merk:',sedan._merk)


# Kita masih bisa mengakses atribut _merk dari luar kelas, <br>karena hal ini hanya bersifat convention alias adat atau kebiasaan saja yang harus disepakati oleh programmer. <br> Di mana jika suatu atribut diawali oleh <font color="red">_</font>, <br>maka ia harusnya tidak boleh diakses kecuali dari internal kelas tersebut <br>atau dari kelas yang mewarisinya.
# 
# Yang harusnya kita lakukan adalah: mengakses atribut protected hanya dari kelas internal atau dari kelas turunan, <br>perhatikan contoh berikut:

# In[38]:


class Mobil:
    def __init__(self, merk):
        self._merk = merk

class MobilBalap(Mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk)
        self._total_gear = total_gear

    def pamer(self):
        # akses _merk dari subclass
        print(
            'Ini mobil',self._merk, 
            'dengan total gear', self._total_gear
        )


# Bikin objek dari kelas MobilBalap:

# In[11]:


ferrari = MobilBalap('Ferrari', 8)
ferrari.pamer()


# <h2 id="private-access-modifier">Private Access Modifier</h2>
# <p>Modifier selanjutnya adalah&nbsp;<em>private</em>. <br>Setiap variabel di dalam suatu kelas yang memiliki hak akses&nbsp;<em>private</em>&nbsp;<br>maka ia&nbsp;<strong>hanya bisa diakses</strong>&nbsp;di dalam kelas tersebut. <br>Tidak bisa diakses dari luar bahkan dari kelas yang mewarisinya.</p>
# <p>Untuk membuat sebuah atribut menjadi&nbsp;<em>private</em>, <br>kita&nbsp;<strong>harus</strong>&nbsp;menambahkan dua buah underscore sebagai&nbsp;<em>prefix</em>&nbsp;nama atribut.</p><br>
# Perhatikan contoh berikut:

# In[13]:


class Mobil:
    def __init__(self, merk):
        self.__merk = merk


# <p>Pad kode di atas, kita telah membuat sebuah atribut dengan nama&nbsp;<span style="color: red;">__merk</span>. <br>Dan karena nama tersebut diawali dua buah underscore, <br>maka ia tidak bisa diakses kecuali dari dalam kelas&nbsp;<span style="color: red;">Mobil</span>&nbsp;saja.</p>
# <p>Mari kita buktikan:</p>

# In[22]:


jip = Mobil('Jeep')
print(f'Merk: {jip.__merk}')


# Kita akan mendapatkan sebuah error sebagai berikut:
# <code class="language-py3" data-lang="py3"><span style="color:#c00;font-weight:bold">AttributeError</span><span style="color:#000;font-weight:bold">:</span> <span style="color:#4e9a06">'Mobil'</span> <span style="color:#204a87">object</span> <span style="color:#000">has</span> <span style="color:#000">no</span> <span style="color:#000">attribute</span> <span style="color:#4e9a06">'__merk'</span>
# </code>
# Tapi jika kita ubah kodenya menjadi seperti ini:

# In[17]:


class Mobil:
    def __init__(self, merk):
        self.__merk = merk

    def tampilkan_merk(self):
        print('Merk:', self.__merk)

jip = Mobil('Jeep')
jip.tampilkan_merk()


# -----------------------------------------------------------------------------------------------------------------------

# <h2 id="accessor-mutator">Accessor Mutator</h2>
# <p>Selanjutnya kita bisa membuat accessor dan mutator atau getter dan setter pada suatu kelas di python.</p>
# <p>Untuk apa accessor dan mutator? Ia adalah sebuah fungsi yang akan dieksekusi ketika kita mengakses (aksesor) suatu atribut pada suatu kelas, atau fungsi yang dieksekusi ketika hendak mengatur (mutator) suatu atribut pada suatu kelas.</p>
# <p>Untuk mendefinisikan accessor (getter), kita perlu mendefinisikan decorator&nbsp;<font color="blue">@property</font>&nbsp;sebelum nama fungsi.</p>
# <p>Sedangkan untuk mengatur mutator (setter), kita perlu mendefinisikan descriptor&nbsp;<font color="blue">@&lt;nama-atribut&gt;.setter</font>.</p>
# <p>Perhatikan contoh berikut:</p>

# In[21]:


class Mobil:
    def __init__(self, tahun):
        self.tahun = tahun

    @property
    def tahun(self):
        return self.__tahun

    @tahun.setter
    def tahun(self, tahun):
        if tahun > 2021:
            self.__tahun = 2021
        elif tahun < 1990:
            self.__tahun = 1990
        else:
            self.__tahun = tahun


# <p>Ketika kita nanti mengakses atribut&nbsp;<span style="color: bule;">tahun&nbsp;(tanpa underscore), maka fungsi&nbsp;<span style="color: bule;">tahun()&nbsp;yang pertama akan dieksekusi.</span></span></p>
# <p>Sedangkan jika kita mengisi / mengubah / memberi nilai pada atribut&nbsp;<span style="color: bule;">tahun&nbsp;(tanpa underscore), maka yang dieksekusi adalah fungsi&nbsp;<span style="color: bule;">tahun()&nbsp;yang kedua.</span></span></p>
# <p>Mari kita coba kode program berikut:</p>

# In[24]:


sedan = Mobil(2200)
print('Mobil ini dibuat tahun',sedan.tahun)


# <p>Kode program di atas akan menampilkan tahun dari sedan yang sudah melalui&nbsp;<font color="blue" >if-else</font>&nbsp;sebelumnya. Sehingga jika kita memberikan nilai&nbsp;<font color="blue">tahun</font>&nbsp;yang lebih dari tahun&nbsp;<font color="blue">2021</font>, yang tersimpan tetaplah tahun&nbsp;<font color="blue">2021</font>.</p>

# <p>Sedangkan jika kita mengakses atribut aslinya yaitu&nbsp;<font  color="red">__tahun</font>, kita akan mendapatkan error karena atribut tersebut bersifat&nbsp;<em>private</em>.</p>

# In[27]:


print('Mobil ini dibuat tahun',sedan.__tahun)


# Akan menampilkan error seperti berikut
# <code class="language-py3" data-lang="py3"><span style="color:#c00;font-weight:bold">AttributeError</span><span style="color:#000;font-weight:bold">:</span> <span style="color:#4e9a06">'Mobil'</span> <span style="color:#204a87">object</span> <span style="color:#000">has</span> <span style="color:#000">no</span> <span style="color:#000">attribute</span> <span style="color:#4e9a06">'__tahun'</span>
# </code>

# Selanjutnya mari kita coba ubah atribut tahun seperti berikut:

# In[30]:


sedan = Mobil(2000)
sedan.tahun = 1800
print('Mobil ini keluaran',sedan.tahun)


# <p>Lihat, kita mengubah tahun menjadi&nbsp;<font color="green">1800</font>&nbsp;akan tetapi yang tersimpan adalah&nbsp;<font color="green">1990</font>. <br>Itu terjadi karena ketika kita mengubah atribut&nbsp;<font color="green">tahun</font>, <br>sistem masih memanggil terlebih dahulu fungsi setter&nbsp;<font color="green">tahun()</font></p>

# <h2 id="menggabungkan-public-protected-dan-private">Menggabungkan Public, Protected, dan Private</h2>
# <p>Selain itu, kita juga bisa menggunakan 3 buah modifiers sekaligus dalam satu kelas, <br>perhatikan contoh berikut:</p>

# In[33]:


class SebuahKelas:
    def __init__(self):
        self.publik = 'Atribut Publik'
        self._protected = 'Atribut Protected'
        self.__privat = 'Atribut Privat'


# <p>Pada contoh di atas kita memiliki 3 buah atribut:</p>
# <ol>
# <li>Atribut&nbsp;<font color="blue">publik</font>&nbsp;dengan modifier&nbsp;<em>public</em></li>
# <li>Atribut&nbsp;<font color="blue">_protected</font>&nbsp;dengan modifier&nbsp;<em>protected</em></li>
# <li>Dan atribut&nbsp;<font color="blue">__privat</font>&nbsp;dengan modifier&nbsp;<em>private</em></li>
# </ol>

# <h2 id="kesimpulan">Kesimpulan</h2>
# <p>Dalam pemrograman python, kita bisa memanfaatkan fitur access modifier untuk mengenkapsulasi sebuah kode program. Alias mengatur mana atribut yang boleh diakses dari luar, dan mana atribut yang hanya konsumsi internal.</p>
# <p>Sayangnya, kelemahan&nbsp;<em>access modifier</em>&nbsp;dalam python adalah:</p>
# <ul>
# <li>Tidak ada atribut yang benar-benar&nbsp;<em>public</em>&nbsp;atau&nbsp;<em>protected</em>. Selama sebuah variabel tidak diawali dua buah&nbsp;<em>underscore</em>, maka ia bisa diakses dari mana pun.</li>
# <li>Hal tersebut menjadikan konsep &ldquo;protected&rdquo; modifier hanyalah sebuah&nbsp;<em>convention</em>&nbsp;atau kebiasaan saja, di mana kalau kita mendefinisikan sebuah atribut yang diawali&nbsp;<strong>satu buah underscore</strong>, maka kita seharusnya tidak mengakses atribut tersebut kecuali dari dalam kelas itu sendiri atau dari kelas turunannya</li>
# </ul>

# In[ ]:




