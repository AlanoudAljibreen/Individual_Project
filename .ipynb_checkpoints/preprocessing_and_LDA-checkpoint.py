def comprehensive_preprocess(text):
    text = str(text)
    text = re.sub(r'http[s]?://\S+', '', text)  # Remove URLs
    text = contractions.fix(text)  # Expand contractions here
    text = text.lower()  # Lowercase
    tokens = word_tokenize(text)  # Tokenize
    tokens = [re.sub(r'[^a-zA-Z\s]', '', token) for token in tokens]  # Remove special characters and digits from each token
    stop_words = set(stopwords.words('english'))
    stop_words.update(['nykaa', 'kay'])
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words and token != '']  # Lemmatize & remove stopwords
    return tokens

def lda_experiments(dictionary, corpus, texts, start=3, limit=20, step=1):
    coherence_values = []
    model_list = []
    topic_numbers = range(start, limit + 1, step)

    for num_topics in topic_numbers:
        model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics,
                         iterations=400, passes=10, random_state=42, per_word_topics=False)
        model_list.append(model)
        coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())
        
        print(f"Completed LDA with {num_topics} topics. Coherence score: {coherencemodel.get_coherence()}")

    # Find the model with the highest coherence score
    best_coherence = max(coherence_values)
    best_model_index = coherence_values.index(best_coherence)
    best_model = model_list[best_model_index]

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(topic_numbers, coherence_values, marker='o')
    plt.title('LDA Coherence Score by Number of Topics')
    plt.xlabel('Number of Topics')
    plt.ylabel('Coherence Score')
    plt.xticks(topic_numbers)
    plt.grid(True)
    plt.show()

    return best_model, best_coherence