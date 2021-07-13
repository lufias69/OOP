import java.util.HashMap;

class Senjata{
    String nama;
    double kekuatan;

    Senjata(String nama, double kekuatan){
        this.nama = nama;
        this.kekuatan = kekuatan;
    }

}

class Karakter{
    String nama;
    int poin;
    double darah;
    HashMap <String, Senjata> senjata = new HashMap<>();

    Karakter(String nama){
        this.nama=nama;
        this.poin = 0;
        this.darah = 100.00;
    }
    void ambil_senjata(String nama_senjata, Senjata senjatanya){
        this.senjata.put(nama_senjata, senjatanya);
    }

    void pukul(Karakter karakter){
        // System.out.println(karakter.darah);
        if (karakter.darah >=0.0){
            this.poin += 4;
            karakter.darah = karakter.darah - 4;

            System.out.println(this.nama+" memukul "+karakter.nama+"  ");
            System.out.println("+ Poin "+this.nama+ " Bertambah Menjadi "+this.poin);
            System.out.println("- Darah "+ karakter.nama+" berkurang menjadi "+karakter.darah);
            System.out.println("------------------------------------------------------------------------------------");
            if (karakter.darah < 0.0){
                karakter.darah = 0;
            }
        }else{
            System.out.println(karakter.nama+" kehabisan darah, Berhenti mi memukul");
        }   
    }

    void pukul(Karakter karakter, String nama_senjata){
        // System.out.println(karakter.darah);
        if (karakter.darah >0.0){
            System.out.println(karakter.darah >=0.0);
            this.poin += 5;
            karakter.darah = karakter.darah - this.senjata.get(nama_senjata).kekuatan;
            if (karakter.darah < 0.0){
                karakter.darah = 0.0;
            }
            System.out.println(this.nama+" memukul "+karakter.nama+" pakai "+nama_senjata+" | berkekuatan "+this.senjata.get(nama_senjata).kekuatan);
            System.out.println("+ Poin "+this.nama+ " Bertambah Menjadi "+this.poin);
            System.out.println("- Darah "+ karakter.nama+" berkurang menjadi "+karakter.darah);
            System.out.println("------------------------------------------------------------------------------------");

        }else{
            System.out.println(karakter.nama+" kehabisan darah, Berhenti mi memukul");
        }
        
        
    }

}





public class App {
    public static void main(String[] args) throws Exception {
        Senjata tas_cewek = new Senjata("Tas Cewek", 5);
        Senjata sapu = new Senjata("Sapu", 7);
         
        Karakter denise = new Karakter("Denise"); 
        denise.ambil_senjata("Tas Cewek", tas_cewek);
        denise.ambil_senjata(sapu.nama, sapu);

        Karakter uya_kuya = new Karakter("Uya Kuya");

        // Aksinya pukul pukulan

        denise.pukul(uya_kuya, "Tas Cewek");
        uya_kuya.pukul(denise);

        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
        denise.pukul(uya_kuya, sapu.nama);
    }
}
