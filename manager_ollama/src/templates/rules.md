### Example of json files

*vmspec.json*
| Name | datatype | Brief description | 
| ---- |----------| ------------------|
| processor_cores | int | number of cores |
| overprovision | int |maximum VM for each core|
| allowSMT | bool |allow Surface-mount technology|
| archs | string |architecture of the system|
| instruction_set | list |processor's instruction set architecture|
| min_cpu_frequency | float |minum processor frequency in expressed in GHz|
| ram_size | int |ram dimension expressed in GB|
| reqECC | bool |request for ecc ram|
| misc | dictionary |OS Infos|
| pci | list of dictionary| GPU specs :<br>- vendor code <br> - model code <br> - quantity <br><br> audio card specs: <br>- vendor code <br> - model code <br> - quantity <br><br> *NB: you can mount a spare audio card but not a spare graphic card, every graphic card has to be mounted along its related audio card*|