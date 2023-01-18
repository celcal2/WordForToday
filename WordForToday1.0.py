import random

ksiegiList = ('Rdz Rodzaju I Mojżesza-50','Wj Wyjścia II Mojżesza-40','Kpł Kapłaństwa III Mojżesza-27',\
'Lb Liczb IV Mojżesza-36','Pwt Powtórzonego Prawa V Mojżesza-34','Jpz Jozuego-24','Sdz Sędziów-21',\
'Rt Rut-4','1 Sm Samuela-31','2 Sm Samuela-24','1 Krl Królewska-22','2 Krl Królewska-25','1 Km Kronik-29',\
'2 Km Kronik-36','Ezd Ezdrasza-10','Ne Nehemiasz-13','Est Estery-10','Hi Hioba-42','Ps Psalmy-150',\
'Prz Przysłów-31','Kz Kaznodziei-10','PnP Pieśń nad Pieśniami-8','Iz Izajasza-66','Jr Jeremiasza-52',\
'LM Lamentacji-5','Ez Ezechiela-48','Dn Daniela-12','Oz Ozeasza-14','Jl Joela-3','Am Amosa-9',\
'Ab Abdiasza-1','Jon Jonasza-4','Mi Micheasza-7','Na Nahuma-3','Ha Habakuka-3','So Sofoniasza-3','Ag Aggeusza-2',\
'Za Zachariasza-14','Ml Maachiasza-4','Mt Mateusza-28','Mk Marka-16','Łk Łukasza-24','J Jana-21','Dz Dzieje Apostolskie-28',\
'Rz Rzymian-16','1 Kor Koryntian-16','2 Kor Koryntian-13','1 Ga Galacjan-6','Ef Efezjan-6',\
'Flp Filipian-4','Kol Kolosan-4','1 Tes Tesaloniczan-5','2 Tes Tesaloniczan-3','1 Tym Tymoteusza-6',\
'2 Tym Tymoteusza-4','Tyt Tytusa-3','Flm Filemona-1','Hbr Hebrajczyków-13','Jk Jakuba-5','1 P Piotra-5',\
'2 P Piotra-3','1 J Jana-5','2 J Jana-1','3 J Jana-1','Jud Judy-1','Obj Objawienia-22')

choosenBook = random.choice(ksiegiList)
choosenBookName = choosenBook.split('-')
choosenBookChepter = random.randint(1,int(choosenBookName[1]))
ileWierszy = int(input(f'Podaj ile jest wierszy w księdze {choosenBookName[0]} w rozdziale {choosenBookChepter}: '))
choosenVerses = random.randint(1,ileWierszy)
print(f'\nSłowo na dzisiaj:\n {choosenBookName[0]}, rozdział {choosenBookChepter}, wiersz {choosenVerses}')