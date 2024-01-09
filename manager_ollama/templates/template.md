### Example of json files

*vmspec.json*
| Name | datatype | Brief description | 
| ---- |----------| ------------------|
| slots | int | number of cores |
| overprovision | int |maximum VM for each core|
| allowSMT | bool |
| archs | string |architecture of the system|
| flags | list |processor's instruction set architecture|
| min_frequency | float |minum processor frequency in expressed in GHz|
| ramsize | int Bytes|ram dimension expressed in Bytes|
| reqECC | bool |request for ecc ram|
| misc | dictionary |OS Infos|
| pci | list of dictionary| graphic card specs :<br>- vendor code <br> - model code <br> - quantity <br><br> audio card specs: <br>- vendor code <br> - model code <br> - quantity <br><br> *NB: you can mount a spare audio card but not a spare graphic card, every graphic card has to be mounted along its related audio card*|   <pre lang=json>"pci": [<br>    {<br>        "vendor": "10de", <br>        "model": "24b0", <br>        "quantity": 1 <br>    },<br>    { <br>        "vendor": "10de",<br>        "model": "228b", <br>        "quantity": 1<br>    }<br>]</pre>|