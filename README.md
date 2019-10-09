# ElGamal-signature-scheme
The ElGamal signature scheme is a digital signature scheme based on the algebraic properties of modular exponentiation, together with the discrete logarithm problem. The algorithm uses a key pair consisting of a public key and a private key. The private key is used to generate a digital signature for a message, and such a signature can be verified by using the signer's corresponding public key. The digital signature provides message authentication (the receiver can verify the origin of the message), integrity (the receiver can verify that the message has not been modified since it was signed) and non-repudiation (the sender cannot falsely claim that they have not signed the message).
## Introduction
Digital signatures serve the same role as traditional pen and ink signatures to provide authentication, confirmation and to associate identities with documents. The signature must be tied to the document mathematically so that it may not be removed and replaced by another or placed on some other document. Cryptographically secure digital signature schemes are formed of two parts, the signing protocol and the authentication process. These processes are designed such that the signature is made using private information but verifiable using only public information that does not compromise the security of the signatory. This requirement explains why digital signature schemes usually stem from public-key cryptosystems.

There is also the concept of a ‘blind signature’ where the signatory is able to sign a document without seeing its content thereby ensuring sender privacy. This is useful in electronic voting systems for endorsing that a vote was made legally without acquiring knowledge of how the vote was cast. Blind signatures are also used in applications of digital cash and cryptocurrencies.

A good digital signature will be impossible to forge, quick to compute and verify and widely applicable. We will consider several digital signature schemes as well as engage in discussion of generalized attacks such as birthday attacks. Note that attacks of this kind are not interested in decrypting messages (which under signature schemes are often already public) but are interested in forging or changing signatures.
## Signing protocol
The signing protocol for an ElGamal signature is as follows. Suppose Alice wants to sign a message, m.

The initial setup is the same as that for ElGamal encryption.

1. Alice chooses a large prime p and a primitive root α.
2. She then chooses a secret integer z and calculates β ≡ αz (mod p).
3. The values of p, α and β are made public and z is kept private.

In order to sign the message m Alice follows the steps below:

1. She selects a secret random integer k such that GCD(k, p – 1) = 1.
2. She then computes r ≡ αk (mod p).
3. She then finally computes s ≡ k-1(m – zr) (mod p – 1).
4. The signed message is the triplet (m, r, s).

The verification process can then be performed by Bob using public information only.

1. Bob computes v1 ≡ (β^r)*(r^s) (mod p) and v2 ≡ (α^m) (mod p).
2. The signature is declared valid if and only if v1 ≡ v2 (mod p).
### Correctness
The verification procedure works by the following argument. Assume that the signature is valid. As s ≡ k-1(m – zr) (mod p – 1), we have sk ≡ (m – zr) (mod p – 1) and hence m ≡ sk + zr (mod p – 1). Therefore by Fermat’s little theorem, that a congruence mod p – 1 in the exponent yields a congruence mod p overall, we have:

v2≡(α^m)≡(α^(s*k+z*r))≡(α^(s*k))*(α^(z*r))≡(β^r)*(r^s)≡v1 (mod p)
