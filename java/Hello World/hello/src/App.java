class User{
    String nama;
    String password;

    User(String inputNama, String inputPassword){
        this.nama = inputNama;
        this.password = inputPassword;
    }
}




public class App {

    // class User{}
    public static void main(String[] args) throws Exception {

        User diana = new User("Diana Ana", "maulogin");

        System.out.println(diana.nama);
        System.out.println(diana.password);
        
    }
}
