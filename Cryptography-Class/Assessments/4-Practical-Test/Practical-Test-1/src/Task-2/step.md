```
┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-2]
└─$ echo "This file was encrypted by Adam Riezqie (NWS23010043)" > message.txt
```

```
┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-2]
└─$ gpg --list-keys
/home/abu/.gnupg/pubring.kbx
----------------------------
pub   rsa4096 2025-05-16 [SC] [expires: 2026-05-16]
      244413E5B46029B88E0FFC399FC18FB47132CDB1
uid           [ultimate] MUHAMMAD ADAM RIEZQIE BIN ALI HIRAHAM <muhammadadam.alihiraham@student.gmi.edu.my>
sub   rsa4096 2025-05-16 [E] [expires: 2026-05-16]


┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-2]
└─$ gpg --encrypt --recipient "MUHAMMAD ADAM RIEZQIE BIN ALI HIRAHAM" message.txt

┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-2]
└─$ ls
message.txt  message.txt.gpg  step.md

┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-2]
└─$ cat message.txt.gpg
�
��U��a���[FO�)ٗ��x�]Q���Jz�:�������>�yU1�?�N �R+��.kܛ�91B&�jQ����
y��I�T�8�r��+^���^��@k}y�'B{'���f�𴗉"T�l�?���O� jBk��H��'@��fq�l_�p�:5 F&�^�6߆�Ax=�
�W�q���~W�c�#�wi�
                 ��+w�?�Q5�_�
                             X1ug(�ִv�=��Z�ϯ�^�֮�i␦�c��,�1�UϐW�4���d��a6'
�R�rR�=��'�ECk}��F=����rt�iJ�\�?��7�Y��p_�A␦�w�a�g��vƛ��KN�q��C�
]d���~
�2I�b[�v�)␦+�4_�EK(�|>pV�[څM�Aq�H����o
x�c����PfU�!��6ɀ�|O�����]4��5g
-��8,|��O�;%?�]8
F{d�1���^��_�̥
             &�q����R�����H���0Lh�`�␦��H�}�kP���5<h�2p�M7-0ީ���M�8�qb��q                                                
┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-2]
└─$
```

```
┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-2]
└─$ gpg --output decrypted.txt --decrypt message.txt.gpg
gpg: encrypted with 4096-bit RSA key, ID 6B618E335CD69A3C, created 2025-05-16
      "MUHAMMAD ADAM RIEZQIE BIN ALI HIRAHAM <muhammadadam.alihiraham@student.gmi.edu.my>"

┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-2]
└─$
```
Enter `passphrase` from task-1

```
┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-2]
└─$ ls
decrypted.txt  message.txt  message.txt.gpg  step.md

┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-2]
└─$ cat decrypted.txt
This file was encrypted by Adam Riezqie (NWS23010043)

┌──(adamriezqie㉿NWS23010043)-[~/…/4-Practical-Test/Practical-Test-1/src/Task-2]
└─$
```