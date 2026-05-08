# Configuração de uma Máquina Virtual com Ubuntu 24.04 LTS

- Este readme é um relatório sobre a criação de uma Máquina Virtual Ubuntu e configuração de Serviços de Rede. Simulamos um servidor acessível pelo Host e por outros dispositivos conectados a mesma rede.

## Máquina Virtual

- Criamos a Máquina Virtual com as especificações necessárias, primeiramente foi mantido o modo NAT para a Máquina utilizar a internet do Host, mas posteriormente foi trocado para o Modo Bridge para testes em rede local.

### Ubuntu Desktop

- Fizemos a instalação apartir da ISO Oficial do Ubuntu, realizando a instalação completa.

## Configuração de Rede e Portas

- Então, redirecionamos as portas do Virtual Box
HTTP: host 8080 → VM 8080
SSH: host 2222 → VM 22

<img src="https://github.com/user-attachments/assets/2f93b3f0-f222-4a0e-bd46-4082c8bdecc3" alt="Port Forwarding">

## Configurando SSH

- Após isso, instalamos e ativamos o serviço SSH via apt, e o Firewall foi configurado, isso garantiria acesso pela porta padrão.

### Testes de Conexão

- Então, testamos a conexão com SSH via Terminal, também testamos o acesso via VS Code, e por fim a conexão foi testada por outro computador conectado a mesma rede.

## Topologia e Comunicação

As Arquiteturas de Rede utilizadas foram as seguintes:
- NAT: A Maquina Virtual acessa a rede através do Host.
- Modo Bridge: A Maquina Virtual se conecta de forma direta a Rede Local.

O principal meio de Transmissão foi a Conexão via Wi-Fi.
Os serviços utilizaram o protocolo IP:
- HTTP de porta 80
- SSH de porta 22

## Análise e Solução de Problemas

- Existiu dificuldade na hora de acessar a Máquina Virtual devido a travamento, foram necessárias duas tentativas de criação da Máquina Ubuntu para a mesma funcionar. Também existiu uma pequena dificuldade no momento de instalação dos Serviços SSH, mas nada anormal.

## Conclusão

- A configuração da Máquina Virtual Ubuntu foi um sucesso. O acesso remoto via SSH e HTTP foram fundamentais para o funcionamento do sistema.
