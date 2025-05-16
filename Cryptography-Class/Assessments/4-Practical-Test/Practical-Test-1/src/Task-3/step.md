```bash
┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-3]
└─$ echo "I, Adam Riezqie, declare this is my work." > signed_message.txt
```

```bash
┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-3]
└─$ gpg --clearsign signed_message.txt

┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-3]
└─$ ls
signed_message.txt  signed_message.txt.asc

┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-3]
└─$ cat signed_message.txt.asc
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

I, Adam Riezqie, declare this is my work.
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCgAdFiEEJEQT5bRgKbiOD/w5n8GPtHEyzbEFAmgnGBIACgkQn8GPtHEy
zbHVaBAAkYQZh3ej+Zk6qFE5T1OCyIhIwjvXcSo5j+0/dJRjU1QGM3ZwDy4B4908
4qQDpX5by/BjwOakasw0u/tc4nI06EMllAKd0Kb4Tm03v6Wyb1f7TpXoXQC6kRjM
qBLlamaPvhCGM1ZKyP9Ym+LyUFwsgaQSJ77v7p3GXhr5uhAwBFlhcf5MBoUwvoxh
l5iQXbbeHv4iDGygTRjUNbxZCsQk5HuKHFZpNW98Aygb+irM5+NoJiPSGGhFfnmS
UqS0vX0lveHQGHyLddAdK1jItl7wjq7A1J7TNk0P22Ugt98wcmmOMDBU1VxrwD/r
vttHsxq+3x3YPY0oAWQymGZJjLsgtBDizNkuOgZel7arbcfONhdKdFSGPDbDhcdl
CGUblhj6byYW9JtkAS2Aw4u8CSXMvuCUDXYbXAOyoOjbuQAYRW8H2r9c+crU21ZJ
/77yKsKKaaztgHp5lGlbrF9eJXLnFv8ujdG4XLV0O/AcCzQ9GM+foeqwWELs9S2C
ClI/kYMOx/Ea5vObp1oElfGyCW2VYX2Umn8Yox84mwV3k3vurPdPh+NU9qtBvLMV
IkTrYm4YnY1SsZp+4ZtEbqy89IFrfetplufHEOl2MhsMzmgq7sSyC+Vyf72/QBbE
B+IdlB/3QyExXwb4cbQVf0lIuL0Jxg+IJzl0ib4awJlEbUjwdw0=
=eYRd
-----END PGP SIGNATURE-----

┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-3]
└─$
```

```bash
┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-3]
└─$ gpg --verify signed_message.txt.asc
gpg: Signature made Fri 16 May 2025 06:48:50 PM +08
gpg:                using RSA key 244413E5B46029B88E0FFC399FC18FB47132CDB1
gpg: Good signature from "MUHAMMAD ADAM RIEZQIE BIN ALI HIRAHAM <muhammadadam.alihiraham@student.gmi.edu.my>" [ultimate]
gpg: WARNING: not a detached signature; file 'signed_message.txt' was NOT verified!
```

```bash
┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-3]
└─$ gpg --detach-sign signed_message.txt

┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-3]
└─$ ls
signed_message.txt  signed_message.txt.asc  signed_message.txt.sig  step.md

┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-3]
└─$ cat signed_message.txt.sig
�3
!$D�`)���9����q2ͱh'�
        ����q2ͱXS�W�l�e��\��W�K��j@�\:J�
                                        V�&�X
��;���!7m*��\���Db����'$^��!T�Nk�#`i/ߘ�Y�n�vԋt��/'�~�0.����ZKX.��ib�ʻ3␦ӛ�U�VgD�����ʟC���������|&c�lJ�ΰ���b�P�!�_�ʄ���!+�6�!F��+|��iOwek��~���<���)
Q���ʪ"7g���&-�y��_�Z�'%�M�qˡ����6�E�M%v-2����V�;<�Z���
�.ocx�w���0�3�9��q�«��ɩ^ssbv���=K�Ej
                                    pMX����o�)�J/�\������1iB2\υl�8/�7!E�C'�*�к��Tu
�җ���[�C��J$��Pf���8�A}��e�                                                                                            
┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-3]
└─$ gpg --verify signed_message.txt.sig signed_message.txt
gpg: Signature made Fri 16 May 2025 06:52:32 PM +08
gpg:                using RSA key 244413E5B46029B88E0FFC399FC18FB47132CDB1
gpg: Good signature from "MUHAMMAD ADAM RIEZQIE BIN ALI HIRAHAM <muhammadadam.alihiraham@student.gmi.edu.my>" [ultimate]

┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-3]
└─$
```