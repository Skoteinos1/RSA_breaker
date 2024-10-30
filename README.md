# RSA_breaker
Proof that RSA is broken<br>

Ever wondered:<br>

How comes that one private key can have multiple public keys?<br>
Or one public key, multiple private keys?<br>
Is there something like universal key?<br>

OR<br>

Why is boss of Telegram sitting at court, but not bosses of Meta, Google or PGP...<br>

You can find answers on first set of questions in my code.<br>

Answer for last question you have to deduce by yourself.<br>

For simple explanation of how RSA works, you could watch these two youtube videos:<br>

https://www.youtube.com/watch?v=4zahvcJ9glg<br>
https://www.youtube.com/watch?v=oOcTVTpUsPQ<br>

How to use this code:<br>
Change option value in line 72 from 1-7.<br>

option 1:<br>
Generates key pairs based on youtube video. It is not optimized, and it uses primes smaller than 100<br>

option 2:<br>
When we have keys, we try to decrypt message with different set of keys<br>

option 3:<br>
In this step we caount which key pair can open most mesasges encrypted by other key pairs

option 4:<br>
Get print out of most succesfull keys

option 5:<br>
Get list of key pairs which can be opened by selected key