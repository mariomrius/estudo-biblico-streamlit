import streamlit as st

def conclusao(titulo="Conclusão:", cor="#C0392B"):
    st.markdown(
        f"<b style='color:{cor}; font-size:20px;'>{titulo}</b>",
        unsafe_allow_html=True
    )

def pergunta(titulo="Conclusão:", cor="#221FCE"):
    st.markdown(
        f"<b style='color:{cor}; font-size:20px;'>{titulo}</b>",
        unsafe_allow_html=True
    )



titulo = st.title("Olá, Abençoado!")
subtitulo = st.subheader("Bem-vindo ao seu estudo bíblico.")
st.write("Aqui você pode explorar as Escrituras, refletir sobre suas mensagens e fortalecer sua fé.")

st.write("Escolha um assunto para começar:")
assuntos = ["", "ESTUDO 1 - Jesus e as Escrituras Sagradas", "ESTUDO 2 - Jesus e o Amor Divino", "ESTUDO 3 - Jesus e a Restauração do Bem",
            "ESTUDO 4 - Jesus e a Oração", "ESTUDO 5 - Jesus e a Salvação", "ESTUDO 6 - Jesus e a Intercessão", "ESTUDO 7 - Jesus e o Destino do Mundo",
            "ESTUDO 8 - Jesus e a Vida Eterna", "ESTUDO 9 - Jesus e o Juízo", "ESTUDO 10 - Jesus e a Lei de Deus", "ESTUDO 11 - Jesus e o Sábado",
            "ESTUDO 12 - Jesus e a Igreja", "ESTUDO 13 - Jesus eo Crescimento Espiritual", "ESTUDO 14 - Jesus e a Fedelidade", "ESTUDO 15 - Jesus e o Batismo",
            "ESTUDO 16 - Jesus e o Estilo de Vida Cristão", "ESTUDO 17 - Jesus e a Missão da Igreja", "ESTUDO 18 - Jesus e o Dom de Profecia",
            "ESTUDO 19 - Jesus e o Espírito Santo", "ESTUDO 20 - Jesus e a Nova Terra" ]
assunto_selecionado = st.selectbox("Selecione um assunto:", assuntos)     
st.write(f"Você selecionou: {assunto_selecionado}")

if assunto_selecionado == "ESTUDO 1 - Jesus e as Escrituras Sagradas":
    st.write("1 - Qual era a fonte de inspiração dos profetas bíblicos? ")
    st.write("2 Pedro 1:21 nos diz que:")
    st.write('A profecia nunca teve origem na vontade humana, mas os homens falaram da parte de Deus, movidos pelo Espírito Santo.')
    conclusao()
    st.write("Isso significa que os profetas foram inspirados por Deus para transmitir Suas mensagens ao povo. " \
            "Eles receberam revelações divinas e foram guiados pelo Espírito Santo para escrever as Escrituras Sagradas. " \
            "Portanto, a fonte de inspiração dos profetas bíblicos foi o próprio Deus, que os usou como instrumentos para comunicar Sua vontade e propósito para a humanidade.")
    
    st.write("2 - Onde se origina a mensagem dos Profetas?")
    st.write("1 Tessalonicenses 2:13 nos diz que:")
    st.write('Quando vocês receberam a palavra de Deus, que ouviram de nós, aceitaram-na não como a palavra dos homens, mas, como realmente é, a palavra de Deus, que atua em vocês que creem.')
    conclusao()
    st.write("A mensagem dos profetas se origina da palavra de Deus. " \
            "Quando as pessoas recebem a palavra de Deus, elas a aceitam como a verdade divina.")
    
    st.write("3 -Toda Bíblia é inspirada?")
    st.write("2 Timóteo 3:16 nos diz que:")
    st.write('Toda a Escritura é inspirada por Deus e útil para o ensino, para a repreensão, para a correção e para a instrução na justiça.')
    conclusao()
    st.write("Sim, toda a Bíblia é inspirada por Deus. " \
            "Ela é útil para o ensino, repreensão, correção e instrução na justiça. " \
            "Portanto, a Bíblia é considerada a palavra de Deus e é fundamental para a fé cristã.")
    
    st .write("4 - O que devemos buscar nas Escrituras?")
    st.write("João 5:39 nos diz que:")
    st.write('Vocês estudam as Escrituras porque pensam que nelas vocês têm a vida eterna. São elas mesmas que testificam a meu respeito.')
    conclusao()
    st.write("Devemos buscar a vida eterna nas Escrituras. " \
            "As Escrituras testificam sobre Jesus Cristo, e é através delas que podemos conhecer a verdade e encontrar a salvação. " \
            "Portanto, é importante estudar as Escrituras para fortalecer nossa fé e compreender a vontade de Deus para nossas vidas.") 
    
    st.write("5 - Quem é o Verbo (ou a Palavra) descrito no evangelho de João?")
    st.write("João 1:1 a 4 e 14 nos diz que:")
    st.write('No princípio era o Verbo, e o Verbo estava com Deus, e o Verbo era Deus. Ele estava no princípio com Deus. Todas as coisas foram feitas por intermédio dele, e sem ele nada do que foi feito se fez. Nele estava a vida, e a vida era a luz dos homens. E o Verbo se fez carne e habitou entre nós, cheio de graça e de verdade; e vimos a sua glória, glória como do unigênito do Pai.')
    conclusao()
    st.write("O Verbo (ou a Palavra) descrito no evangelho de João é Jesus Cristo. " \
            "Ele é descrito como estando no princípio com Deus, sendo Deus e sendo o agente da criação. " \
            "O Verbo se fez carne e habitou entre nós, revelando a glória de Deus. " \
            "Portanto, Jesus é a manifestação da Palavra de Deus e é central para a fé cristã.")
    
    st.write("6 - Que método Deus usou para criar todas as coisas?")
    st.write("Salmos 33:9 nos diz que:")
    st.write('Pois ele falou, e tudo se fez; ele ordenou, e tudo passou a existir.')
    conclusao()
    st.write("Deus usou o método da palavra para criar todas as coisas. " \
            "Ele falou e tudo se fez, Ele ordenou e tudo passou a existir. "\
            "Portanto, a criação foi realizada através da palavra de Deus, demonstrando Seu poder e autoridade sobre toda a criação.")  
    
    st.write("7 - Por que Jesus se admirou com a resposta do centurião?")
    st.write("Mateus 8:8 - 10 nos diz que:")
    st.write("O centurião respondeu:" "Senhor, não sou digno de que entres debaixo do meu telhado, mas apenas dize a palavra, e o meu servo será curado."  \
             "Porque também eu sou homem sujeito à autoridade, tendo soldados sob meu comando. Digo a um: Vá, e ele vai; e a outro: Venha, e ele vem; e a um servo: Faça isso, e ele faz." \
             "Quando Jesus ouviu isso, ficou admirado e disse aos que o seguiam: ""Digo a verdade a vocês, nem mesmo em Israel encontrei tamanha fé.")
    conclusao()
    st.write("Jesus elogiou a fé do centurião, afirmando que não havia encontrado tamanha fé nem mesmo em Israel. " \
            "Isso destaca a importância da fé na vida cristã e o impacto que ela pode ter na realização dos propósitos de Deus.")       

    st.write("8 - Como Jesus interpretava as Escrituras?")
    st.write("Lucas 24:27 nos diz que:")
    st.write('E, começando por Moisés e por todos os profetas, explicou-lhes o que constava a respeito dele em todas as Escrituras.')
    conclusao()
    st.write("Jesus interpretava as Escrituras começando por Moisés e por todos os profetas, explicando o que constava a respeito dele em todas as Escrituras. " \
            "Ele mostrava como as Escrituras apontavam para Ele como o Messias e o Salvador. " \
            "Portanto, Jesus tinha uma compreensão profunda das Escrituras e as usava para revelar a verdade sobre si mesmo e sobre o plano de salvação de Deus.")  
    

elif assunto_selecionado == "ESTUDO 2 - Jesus e o Amor Divino":
    st.write("Conteúdo do ESTUDO 2 - Jesus e o Amor Divino")
elif assunto_selecionado == "ESTUDO 3 - Jesus e a Restauração do Bem":
    st.write("Conteúdo do ESTUDO 3 - Jesus e a Restauração do Bem")
elif assunto_selecionado == "ESTUDO 4 - Jesus e a Oração":
    st.write("Conteúdo do ESTUDO 4 - Jesus e a Oração")
elif assunto_selecionado == "ESTUDO 5 - Jesus e a Salvação":
    st.write("Conteúdo do ESTUDO 5 - Jesus e a Salvação")
elif assunto_selecionado == "ESTUDO 6 - Jesus e a Intercessão":
    st.write("Conteúdo do ESTUDO 6 - Jesus e a Intercessão")
elif assunto_selecionado == "ESTUDO 7 - Jesus e o Destino do Mundo":
    st.write("Conteúdo do ESTUDO 7 - Jesus e o Destino do Mundo")
elif assunto_selecionado == "ESTUDO 8 - Jesus e a Vida Eterna":
    st.write("Conteúdo do ESTUDO 8 - Jesus e a Vida Eterna")
elif assunto_selecionado == "ESTUDO 9 - Jesus e o Juízo":
    st.write("Conteúdo do ESTUDO 9 - Jesus e o Juízo")
elif assunto_selecionado == "ESTUDO 10 - Jesus e a Lei de Deus":
    st.write("Conteúdo do ESTUDO 10 - Jesus e a Lei de Deus")
elif assunto_selecionado == "ESTUDO 11 - Jesus e o Sábado":
    st.write("Conteúdo do ESTUDO 11 - Jesus e o Sábado")
elif assunto_selecionado == "ESTUDO 12 - Jesus e a Igreja":
    st.write("Conteúdo do ESTUDO 12 - Jesus e a Igreja")
elif assunto_selecionado == "ESTUDO 13 - Jesus eo Crescimento Espiritual":
    st.write("Conteúdo do ESTUDO 13 - Jesus eo Crescimento Espiritual")
elif assunto_selecionado == "ESTUDO 14 - Jesus e a Fedelidade":
    st.write("Conteúdo do ESTUDO 14 - Jesus e a Fedelidade")
elif assunto_selecionado == "ESTUDO 15 - Jesus e o Batismo":
    st.write("Conteúdo do ESTUDO 15 - Jesus e o Batismo")
elif assunto_selecionado == "ESTUDO 16 - Jesus e o Estilo de Vida Cristão":
    st.write("Conteúdo do ESTUDO 16 - Jesus e o Estilo de Vida Cristão")
elif assunto_selecionado == "ESTUDO 17 - Jesus e a Missão da Igreja":
    st.write("Conteúdo do ESTUDO 17 - Jesus e a Missão da Igreja")
elif assunto_selecionado == "ESTUDO 18 - Jesus e o Dom de Profecia":
    st.write("Conteúdo do ESTUDO 18 - Jesus e o Dom de Profecia")
elif assunto_selecionado == "ESTUDO 19 - Jesus e o Espírito Santo":
    st.write("Conteúdo do ESTUDO 19 - Jesus e o Espírito Santo")
elif assunto_selecionado == "ESTUDO 20 - Jesus e a Nova Terra":
    st.write("Conteúdo do ESTUDO 20 - Jesus e a Nova Terra")



