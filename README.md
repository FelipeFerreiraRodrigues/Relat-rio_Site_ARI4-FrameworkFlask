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

# Servidor Criado para Acesso
### (Leitura Opcional)

## Código Python

<img width="1660" height="712" alt="Captura de tela 2026-05-08 080235" src="https://github.com/user-attachments/assets/3ec7e42d-30a5-48bb-afbc-a170dc2512dc" />

- Este se trata do código Python FrameworkFlask escrito para acesso
- Além das funções principais entregues pelo Professor em aula, fiz com que caso o usuário não tenha acessado o sistema com o Login e Senha necessário e tentasse acessar as demais rotas, fosse redirecionado a página de Login original.

### Funcionamento do Servidor

- Aqui estão prints do Servidor em funcionamento

<img width="1919" height="1028" alt="Captura de tela 2026-05-08 080340" src="https://github.com/user-attachments/assets/944fc26a-275e-4d5a-bafe-77d11c881011" />
<img width="1919" height="1030" alt="Captura de tela 2026-05-08 080404" src="https://github.com/user-attachments/assets/27b8bd6d-d66c-4c9b-8995-fd674f9dc4d4" />
<img width="1919" height="1030" alt="Captura de tela 2026-05-08 080420" src="https://github.com/user-attachments/assets/8b224e36-a20f-4f8a-89d2-d66a2ccbbd22" />
