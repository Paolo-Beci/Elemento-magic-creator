# Manager Ollama
Questo servizio si occupa di gestire il servizio ollama in modo da poter generare un json di una configurazione (inerente ad un certo programma) compatibile con lo stack di Elemento. 
Attualmente il servizio si basa su un modello llama2 (versione 13b). Se si vuole utilizzare un modello diverso è necessario modificare il file `manager_ollama/utils/ollama_utils.py` e modificare la variabile `llama2_version` con la versione desiderata.

## APIs
- /api/v1/check-server
  - **GET**: Controlla se il server è pronto per essere utilizzato.
- /api/v1/pull/llama2?params
  - Il paraemtro `params` è opzionale e può essere utilizzato per specificare il numero di parametri da utilizzare nel modello llama2 (default = 13b). Per dettagli vedere la lista di [versioni disponibili](https://ollama.ai/library/llama2/tags).
  - **POST**: Effettua il pull del modello llama2.
- /api/v1/generate?direct={true | false}
  - Il parametro `direct` (default = false) è opzionale e può essere utilizzato per specificare se generare direttamente il json di configurazione (true) o se effettuare un refinement del testo (false), questo step implica una chiamata aggiuntiva verso Ollama.
  - **GET**: Genera il json di configurazione.

## Setup
*Last update: 12/01/2024*

### Nvidia drivers
Necessario (per ottenere performance accettabili) che il server sia dotato di GPU Nvidia e che siano installati i driver Nvidia. Per `almalinux` fare riferimento a [HowTo/NVIDIA](https://rpmfusion.org/Howto/NVIDIA#About_this_Howto), di seguito un esempio di installazione per `almalinux 9.3` per una NVIDIA GV100GL [Tesla V100 PCIe 16GB]:
```
sudo dnf install --nogpgcheck https://dl.fedoraproject.org/pub/epel/epel-release-latest-$(rpm -E %rhel).noarch.rpm
sudo dnf install --nogpgcheck https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-$(rpm -E %rhel).noarch.rpm https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-$(rpm -E %rhel).noarch.rpm
sudo dnf install akmod-nvidia # rhel/centos users can use kmod-nvidia instead
sudo dnf install xorg-x11-drv-nvidia-cuda
```

### Nvidia Container Toolkit
Necessario installare il toolkit di nvidia dedicato ai container([nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)).
- Configurazione del repository
```
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo \
    | sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```
- Installazione del toolkit
```
sudo yum install -y nvidia-container-toolkit
```

### Docker setup
Per far si che i container possano accedere alle GPU è necessario configurare docker per far si che possa utilizzare il toolkit di nvidia.
```
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

### Docker-compose
- Necessario definire questo servizio nella stessa rete del servizio ollama (tramite docker networking) definendo come hostname `ollama`. Di seguito un esempio di docker-compose inerente a questi due servizi.
```
  manager-ollama:
    build: ./manager_ollama
    container_name: manager-ollama
    hostname: manager-ollama
    networks:
      - net
    restart: unless-stopped

  ollama:
    image: ollama/ollama
    container_name: ollama
    hostname: ollama
    volumes:
      - ollama_data:/root/.ollama
    networks:
      - net
    restart: unless-stopped
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

## ToDo
- [ ] Aggiungere il supporto per le schede audio.