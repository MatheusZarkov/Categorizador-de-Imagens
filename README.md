# Categorizador de Imagens para Obsidian
## Documentação

### Objetivo
Este script ajuda a organizar imagens para o Obsidian, criando automaticamente notas markdown categorizadas sempre que uma imagem é adicionada a uma pasta monitorada. É particularmente útil para gerenciar imagens que serão usadas no Obsidian Canvas.

### Requisitos de Instalação
1. **Instalação do Python**
   - Python 3.x necessário
   - Pacote necessário: `watchdog` (instale usando `pip install watchdog`)

2. **Estrutura de Pastas**
```
📁 Seu_Vault_Obsidian/
├── 📁 Assets/              # Onde seu script vai monitorar
│   ├── 📄 script.py       # O script em si
│   └── 📁 Prompts/        # Criado automaticamente
│       ├── 📁 Girls/
│       ├── 📁 Medieval/
│       ├── 📁 Random/
│       └── 📁 Style/
```

### Passos para Instalação
1. Crie uma pasta `Assets` no seu vault do Obsidian se ainda não tiver
2. Coloque o script (`script.py`) dentro da pasta `Assets`
3. Abra o terminal/prompt de comando
4. Navegue até sua pasta Assets
5. Execute: `pip install watchdog`
6. Execute o script: `python script.py`

### Como Funciona
1. **Monitoramento**: O script monitora continuamente a pasta `Assets` para novas imagens
2. **Detecção de Imagem**: Quando uma nova imagem é adicionada, o script é acionado
3. **Janela de Entrada**: Uma caixa de diálogo aparece com:
   - Quatro botões de categoria (Girls, Medieval, Random, Style)
   - Campo de texto para notas
4. **Criação da Nota**: 
   - Selecione uma categoria clicando em um dos botões
   - Digite o conteúdo da sua nota
   - Pressione Enter ou clique no botão da categoria
5. **Organização de Arquivos**:
   - Cria uma nota markdown na pasta da categoria escolhida
   - A nota inclui seu texto e um link de imagem do Obsidian
   - Formato: `seu_texto_da_nota\n\n![[nome_da_imagem.extensão]]`

### Exemplo de Uso
1. Inicie o script
2. Arraste uma imagem (ex: `exemplo.jpg`) para a pasta `Assets`
3. Janela de entrada aparece
4. Digite sua nota (ex: "Imagem de referência para castelo medieval")
5. Clique no botão "Medieval"
6. Resultado: Cria `exemplo.md` em `Prompts/Medieval/` contendo:
```markdown
Imagem de referência para castelo medieval

![[exemplo.jpg]]
```

### Notas Importantes
- Mantenha o script rodando enquanto trabalha com imagens
- As imagens permanecem na pasta Assets
- Apenas as notas markdown são organizadas em categorias
- Compatível com a maioria dos formatos de imagem (jpg, png, webp, etc.)
- Funciona com a sintaxe de incorporação de imagens do Obsidian
- Perfeito para organizar referências do Canvas

### Solução de Problemas
- Se a janela não fechar: Certifique-se de digitar texto antes de selecionar a categoria
- Se as notas não forem criadas: Verifique as permissões da pasta
- Se as imagens não forem detectadas: Verifique se o arquivo é um formato de imagem válido

### Melhores Práticas
1. Mantenha o script rodando em segundo plano enquanto trabalha
2. Use notas descritivas para melhor organização
3. Verifique regularmente as pastas de categorias
4. Faça backup do seu vault regularmente

### Requisitos de Localização do Script
O script DEVE ser colocado na pasta onde você quer monitorar as imagens. Tipicamente, seria a pasta Assets ou Images do seu vault do Obsidian.

### Atalhos de Teclado
- Enter: Enviar nota após selecionar categoria
- Fechar janela: Alt+F4 (Windows) ou Cmd+Q (Mac)

Este script é particularmente útil para:
- Organizar imagens de referência para o Obsidian Canvas
- Manter documentação estruturada de imagens
- Categorização rápida de recursos visuais
- Criar notas de imagem consistentes

Lembre-se de ajustar a estrutura de pastas de acordo com o sistema de organização do seu vault do Obsidian.
