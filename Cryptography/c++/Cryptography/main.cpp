#include <iostream>
#include <string>
#include <cryptopp/osrng.h>
#include <cryptopp/rsa.h>
#include <cryptopp/hex.h>
#include <cryptopp/files.h>

using namespace CryptoPP;
using namespace std;

int main() {
    AutoSeededRandomPool rng;

    // Sinh cặp khóa RSA 2048 bit
    InvertibleRSAFunction params;
    params.GenerateRandomWithKeySize(rng, 2048);

    RSA::PrivateKey privateKey(params);
    RSA::PublicKey publicKey(params);

    // Tạo bộ mã hóa với public key
    RSAES_OAEP_SHA_Encryptor encryptor(publicKey);

    string message = "Hello world!";
    string cipher, recovered;

    // Mã hóa
    StringSource ss1(message, true,
        new PK_EncryptorFilter(rng, encryptor,
            new StringSink(cipher)
        ) // PK_EncryptorFilter
    ); // StringSource

    // In ciphertext dạng hex để xem
    cout << "Cipher (hex): ";
    StringSource(cipher, true,
        new HexEncoder(new FileSink(cout))
    );
    cout << endl;

    // Tạo bộ giải mã với private key
    RSAES_OAEP_SHA_Decryptor decryptor(privateKey);

    // Giải mã trực tiếp từ ciphertext binary
    StringSource ss2(cipher, true,
        new PK_DecryptorFilter(rng, decryptor,
            new StringSink(recovered)
        )
    );

    cout << "Recovered: " << recovered << endl;
    return 0;
}
