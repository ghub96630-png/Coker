FROM kalilinux/kali-rolling:latest

ENV DEBIAN_FRONTEND=noninteractive

# അത്യാവശ്യമായ കോർ ടൂളുകളും പൈത്തണും മാത്രം ഇൻസ്റ്റാൾ ചെയ്യുന്നു (Heavy packages ഒഴിവാക്കിയിരിക്കുന്നു)
RUN apt-get update && apt-get install -y \
    kali-linux-core \
    nmap \
    python3 \
    python3-requests \
    sudo \
    zsh \
    git \
    curl \
    openssh-server \
    procps \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# അഡ്മിൻ യൂസർ സെറ്റപ്പ്
RUN useradd -m -s /usr/bin/zsh hacker && \
    echo 'hacker:hacker123' | chpasswd && \
    usermod -aG sudo hacker && \
    echo "hacker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# സ്ക്രിപ്റ്റ് സിസ്റ്റത്തിലേക്ക് കോപ്പി ചെയ്യുന്നു
COPY upload_backup.py /home/hacker/upload_backup.py
RUN chmod +x /home/hacker/upload_backup.py

RUN ssh-keygen -A && mkdir -p /var/run/sshd

USER hacker
WORKDIR /home/hacker
