# BotnetDetection
This repository focuses on botnet detection using machine learning techniques.
Botnet is any collection of compromised PCs controlled by an attacker remotely, more like a “virtual robot army.” The individual PCs that are part of a botnet are known as “bots” or “zombies,” and their owners may not even know they're being used in attack.

Dataset - https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-42/
This is a dataset of botnet traffic that was captured in the CTU University in 2011.
It has a large capture of real botnet traffic mixed with normal traffic.
The dataset contains 40961 rows, 33 columns and contains fields like source address, destination address, port number, source rate, destination rate, label and many other fields giving the network information.
The pre-processing on the dataset is done in order to remove the fields which will not play a significant role in detection of botnets.

It uses the decision tree classifier and naive bayes classifier present in sklearn(machine learning library).
The accuracy score of decision tree is obtained as 99.0% while naive bays model gave an accuracy score of 94.0%
Reference - https://github.com/ShehzadaAlam/Botnet-Detection/blob/master/Botnet%20Detection.ipynb
