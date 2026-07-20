FROM kalilinux/kali-rolling:latest

ENV DEBIAN_FRONTEND=noninteractive

# ഏറ്റവും അത്യാവശ്യമായ പാക്കേജുകൾ മാത്രം ഇൻസ്റ്റാൾ ചെയ്യുന്നു (Errors ഒഴിവാക്കാൻ)
RUN apt-get update && apt-get install -y \
    kali-linux-core \
    sudo \
    zsh \
    git \
    curl \
    python3 \
    python3-requests \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# യൂസർ സെറ്റപ്പ്
RUN useradd -m -s /usr/bin/zsh hacker && \
    echo 'hacker:hacker123' | chpasswd && \
    usermod -aG sudo hacker && \
    echo "hacker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER hacker
WORKDIR /home/hacker
