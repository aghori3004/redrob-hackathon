# Submission top-N — labeling worksheet

Assign a tier 0–5 per eval/rubric.md. Rank shown for context only; judge the profile, not the rank.


---

**model rank #1**

### CAND_0077337  [submission_top]
**Staff Machine Learning Engineer** @ Paytm (Fintech, 10001+) | 7.0y | Kochi, Kerala, India
_Summary:_ Senior AI engineer with 7.0 years of hands-on experience building production ML systems, with a focus on search, retrieval, and ranking. Most recently, I designed the company's first hybrid retrieval system combining BM25 with dense vector recall, serving 50M+ queries per month. My day-to-day work spans embedding model selection and fine-tuning, hybrid retrieval architecture, learning-to-rank, behavioral-signal integration, and the offline/online evaluation that ties it all together. I've shipped systems in both early-stage product companies and at larger scale, and I've spent enough time on both that I know which tradeoffs apply where. I care more about shipping a working system in 6 weeks than a theoretically perfect one in 6 months. Currently exploring my next move — looking for senior IC or tech-lead roles where I can own the intelligence layer end-to-end.
_Career:_
- Staff Machine Learning Engineer @ Paytm (Fintech, 10001+, 19mo, current): Built and shipped a production recommendation system at a marketplace product, going from offline experimentation to live A/B test in 5 months. The system combined collaborative filtering (matrix factorization), content-based features (TF-IDF + sentence-transformer embeddings), and a behavioral re-ranking layer. The most interesting technical challenge was the cold-start problem for new users; I designed an exploration-exploitation policy using Thompson sampling that improved new-user retention by 11% in the first month.
- Senior NLP Engineer @ Razorpay (Fintech, 1001-5000, 14mo): Owned the design and rollout of a large-scale semantic search system serving an internal corpus of 35M+ items. Migrated the existing BM25-only retrieval to a hybrid setup combining sparse and dense vectors (sentence-transformers, MPNet-base initially, later fine-tuned BGE-large for our domain). The new system reduced p95 retrieval latency by 60% while improving NDCG@10 by 18% on our held-out eval set. Spent substantial time on the boring-but-critical parts: incremental index refresh, embedding drift monitoring, online/offline metric correlation. Led a team of 4 engineers across the rollout.
- Senior NLP Engineer @ Glance (AI/ML, 501-1000, 44mo): Led the migration from keyword-based to embedding-based search across a 30M+ candidate corpus over 8 months. Designed three successive ranker variants and ran them in A/B testing alongside the legacy keyword system. The final embedding ranker improved recruiter engagement metrics by 24% and reduced the average time-to-shortlist by 38%. Most of the engineering effort went into the boring infrastructure: index versioning, embedding versioning, rollback paths, and the dashboards that let recruiters trust the new system. Mentored two junior engineers through this rollout.
- Senior AI Engineer @ Aganitha (AI/ML, 51-200, 6mo): Led the migration from keyword-based to embedding-based search across a 30M+ candidate corpus over 8 months. Designed three successive ranker variants and ran them in A/B testing alongside the legacy keyword system. The final embedding ranker improved recruiter engagement metrics by 24% and reduced the average time-to-shortlist by 38%. Most of the engineering effort went into the boring infrastructure: index versioning, embedding versioning, rollback paths, and the dashboards that let recruiters trust the new system. Mentored two junior engineers through this rollout.
_Edu:_ B.Tech Computer Engineering, Georgia Tech (tier_1)
_Signals:_ last_active 2026-05-26, response_rate 0.95, open_to_work True, notice 60d, relocate True, interview_completion 0.73, github 68.0

`tier: ___`  notes: 


---

**model rank #2**

### CAND_0064326  [submission_top]
**Search Engineer** @ Sarvam AI (AI/ML, 51-200) | 7.6y | Gurgaon, Haryana, India
_Summary:_ Machine learning engineer with 7.6 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I shipped our first RAG-based feature this year and now own the eval framework for it. I've spent enough time debugging production ranking issues to know which signals matter and which are noise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Search Engineer @ Sarvam AI (AI/ML, 51-200, 31mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- Machine Learning Engineer @ Aganitha (AI/ML, 51-200, 24mo): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
- Machine Learning Engineer @ Freshworks (SaaS, 5001-10000, 24mo): Implemented a RAG-based customer support chatbot integrated with our existing ticketing system. Built the document ingestion pipeline (chunking, embedding via OpenAI embeddings, storing in Pinecone) and the answer-generation layer (initially GPT-4, then a fine-tuned smaller model for cost control). Designed the evaluation framework with both automatic metrics (BLEU, ROUGE) and human-in-the-loop quality scores. Deployment cut average ticket resolution time by 31% for the supported categories.
- Machine Learning Engineer @ Apple (Consumer Electronics, 10001+, 12mo): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
_Edu:_ B.Tech Computer Science, COEP Pune (tier_2)
_Signals:_ last_active 2026-05-21, response_rate 0.94, open_to_work True, notice 45d, relocate False, interview_completion 0.9, github 61.4

`tier: ___`  notes: 


---

**model rank #3**

### CAND_0014440  [submission_top]
**Recommendation Systems Engineer** @ CRED (Fintech, 1001-5000) | 6.4y | Chennai, Tamil Nadu, India
_Summary:_ Machine learning engineer with 6.4 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. Along the way I've gotten comfortable with the operational side — A/B testing, drift monitoring, retraining schedules. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Recommendation Systems Engineer @ CRED (Fintech, 1001-5000, 31mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- NLP Engineer @ Freshworks (SaaS, 5001-10000, 31mo): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- NLP Engineer @ upGrad (EdTech, 1001-5000, 14mo): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
_Edu:_ B.Tech Data Science, VJTI Mumbai (tier_2)
_Edu:_ Ph.D Machine Learning, Massachusetts Institute of Technology (tier_1)
_Signals:_ last_active 2026-05-10, response_rate 0.64, open_to_work True, notice 60d, relocate False, interview_completion 0.84, github 89.5

`tier: ___`  notes: 


---

**model rank #4**

### CAND_0041610  [submission_top]
**Recommendation Systems Engineer** @ Zoho (SaaS, 10001+) | 6.7y | Indore, Madhya Pradesh, India
_Summary:_ Machine learning engineer with 6.7 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. I care a lot about evaluation rigor — too many teams ship models without offline benchmarks they trust. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Recommendation Systems Engineer @ Zoho (SaaS, 10001+, 31mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- Applied ML Engineer @ Observe.AI (AI/ML, 201-500, 26mo): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
- Search Engineer @ InMobi (AdTech, 1001-5000, 15mo): Implemented a RAG-based customer support chatbot integrated with our existing ticketing system. Built the document ingestion pipeline (chunking, embedding via OpenAI embeddings, storing in Pinecone) and the answer-generation layer (initially GPT-4, then a fine-tuned smaller model for cost control). Designed the evaluation framework with both automatic metrics (BLEU, ROUGE) and human-in-the-loop quality scores. Deployment cut average ticket resolution time by 31% for the supported categories.
- Machine Learning Engineer @ Swiggy (Food Delivery, 5001-10000, 7mo): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
_Edu:_ B.Tech Information Technology, SRM University (tier_2)
_Edu:_ M.Tech Computer Science, Lovely Professional University (tier_3)
_Signals:_ last_active 2026-05-14, response_rate 0.52, open_to_work True, notice 30d, relocate True, interview_completion 0.8, github 52.1

`tier: ___`  notes: 


---

**model rank #5**

### CAND_0061265  [submission_top]
**Recommendation Systems Engineer** @ Zoho (SaaS, 10001+) | 6.6y | Delhi, Delhi, India
_Summary:_ Machine learning engineer with 6.6 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. I've learned that most retrieval problems are actually evaluation problems in disguise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Recommendation Systems Engineer @ Zoho (SaaS, 10001+, 20mo, current): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
- Senior Data Scientist @ Observe.AI (AI/ML, 201-500, 36mo): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
- Senior Data Scientist @ Paytm (Fintech, 10001+, 22mo): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
_Edu:_ B.E. Data Science, IIT Madras (tier_1)
_Signals:_ last_active 2026-03-25, response_rate 0.94, open_to_work True, notice 120d, relocate False, interview_completion 0.57, github 79.8

`tier: ___`  notes: 


---

**model rank #6**

### CAND_0041669  [submission_top]
**Recommendation Systems Engineer** @ CRED (Fintech, 1001-5000) | 8.0y | Noida, Uttar Pradesh, India
_Summary:_ Machine learning engineer with 8.0 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I shipped our first RAG-based feature this year and now own the eval framework for it. I've spent enough time debugging production ranking issues to know which signals matter and which are noise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Recommendation Systems Engineer @ CRED (Fintech, 1001-5000, 37mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- Search Engineer @ Mad Street Den (AI/ML, 201-500, 52mo): Implemented a RAG-based customer support chatbot integrated with our existing ticketing system. Built the document ingestion pipeline (chunking, embedding via OpenAI embeddings, storing in Pinecone) and the answer-generation layer (initially GPT-4, then a fine-tuned smaller model for cost control). Designed the evaluation framework with both automatic metrics (BLEU, ROUGE) and human-in-the-loop quality scores. Deployment cut average ticket resolution time by 31% for the supported categories.
- NLP Engineer @ Yellow.ai (AI/ML, 201-500, 6mo): Built a content recommendation system serving 10M+ users that combined collaborative filtering with content-based ranking. The system uses item-item similarity (via sentence-transformer embeddings) for cold starts and a gradient-boosted model trained on engagement signals for warm users. Most of my time went into the feature pipeline (~200 features) and the A/B testing infrastructure. The launch improved 7-day retention by 6% and time spent per session by 14%.
_Edu:_ B.Tech Information Technology, IIT Guwahati (tier_1)
_Edu:_ B.E. Computer Engineering, IIT Guwahati (tier_1)
_Signals:_ last_active 2026-04-06, response_rate 0.77, open_to_work True, notice 60d, relocate False, interview_completion 0.93, github 70.9

`tier: ___`  notes: 


---

**model rank #7**

### CAND_0044222  [submission_top]
**AI Engineer** @ PolicyBazaar (Insurance Tech, 5001-10000) | 7.7y | Vizag, Andhra Pradesh, India
_Summary:_ Machine learning engineer with 7.7 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. I care a lot about evaluation rigor — too many teams ship models without offline benchmarks they trust. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- AI Engineer @ PolicyBazaar (Insurance Tech, 5001-10000, 49mo, current): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
- AI Engineer @ InMobi (AdTech, 1001-5000, 43mo): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
_Edu:_ M.Sc Machine Learning, IISc Bangalore (tier_1)
_Signals:_ last_active 2026-05-15, response_rate 0.6, open_to_work True, notice 60d, relocate False, interview_completion 0.89, github 28.9

`tier: ___`  notes: 


---

**model rank #8**

### CAND_0081846  [submission_top]
**Lead AI Engineer** @ Razorpay (Fintech, 1001-5000) | 6.7y | Jaipur, Rajasthan, India
_Summary:_ Senior AI engineer with 6.7 years of hands-on experience building production ML systems, with a focus on search, retrieval, and ranking. Most recently, I rebuilt the candidate-JD matching pipeline from scratch, taking it from 0.72 to 0.91 NDCG@10, serving 50M+ queries per month. My day-to-day work spans embedding model selection and fine-tuning, hybrid retrieval architecture, learning-to-rank, behavioral-signal integration, and the offline/online evaluation that ties it all together. I've shipped systems in both early-stage product companies and at larger scale, and I've spent enough time on both that I know which tradeoffs apply where. I have strong opinions about when LLMs are the right hammer and when classical IR is — usually it's both. Currently exploring my next move — looking for senior IC or tech-lead roles where I can own the intelligence layer end-to-end.
_Career:_
- Lead AI Engineer @ Razorpay (Fintech, 1001-5000, 27mo, current): Built a RAG-based ranking pipeline serving 50M+ queries per month for an internal recruiter-facing search product. The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. Designed the offline evaluation framework from scratch — NDCG, MRR, recall@K calibrated against online A/B engagement metrics. Drove the migration over 4 months including the recruiter-feedback loop that surfaced reranking edge cases.
- Senior Machine Learning Engineer @ Paytm (Fintech, 10001+, 52mo): Owned the design and rollout of a large-scale semantic search system serving an internal corpus of 35M+ items. Migrated the existing BM25-only retrieval to a hybrid setup combining sparse and dense vectors (sentence-transformers, MPNet-base initially, later fine-tuned BGE-large for our domain). The new system reduced p95 retrieval latency by 60% while improving NDCG@10 by 18% on our held-out eval set. Spent substantial time on the boring-but-critical parts: incremental index refresh, embedding drift monitoring, online/offline metric correlation. Led a team of 4 engineers across the rollout.
_Edu:_ B.E. Data Science, IIT Hyderabad (tier_1)
_Edu:_ Ph.D Computer Engineering, IIT Delhi (tier_1)
_Signals:_ last_active 2026-05-03, response_rate 0.73, open_to_work True, notice 30d, relocate True, interview_completion 0.94, github 33.7

`tier: ___`  notes: 


---

**model rank #9**

### CAND_0050454  [submission_top]
**AI Engineer** @ Rephrase.ai (AI/ML, 11-50) | 6.8y | Delhi, Delhi, India
_Summary:_ Machine learning engineer with 6.8 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. I care a lot about evaluation rigor — too many teams ship models without offline benchmarks they trust. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- AI Engineer @ Rephrase.ai (AI/ML, 11-50, 30mo, current): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
- Machine Learning Engineer @ Uber (Transportation, 10001+, 20mo): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- Machine Learning Engineer @ Adobe (Software, 10001+, 31mo): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
_Edu:_ M.S. Machine Learning, Bharati Vidyapeeth (tier_3)
_Edu:_ Ph.D Data Science, IIT Kanpur (tier_1)
_Signals:_ last_active 2026-04-27, response_rate 0.77, open_to_work True, notice 30d, relocate True, interview_completion 0.72, github -1

`tier: ___`  notes: 


---

**model rank #10**

### CAND_0018499  [submission_top]
**Senior Machine Learning Engineer** @ Zomato (Food Delivery, 5001-10000) | 7.2y | Noida, Uttar Pradesh, India
_Summary:_ Senior AI engineer with 7.2 years of hands-on experience building production ML systems, with a focus on search, retrieval, and ranking. Most recently, I designed the company's first hybrid retrieval system combining BM25 with dense vector recall, serving 50M+ queries per month. My day-to-day work spans embedding model selection and fine-tuning, hybrid retrieval architecture, learning-to-rank, behavioral-signal integration, and the offline/online evaluation that ties it all together. I've shipped systems in both early-stage product companies and at larger scale, and I've spent enough time on both that I know which tradeoffs apply where. I have strong opinions about when LLMs are the right hammer and when classical IR is — usually it's both. Currently exploring my next move — looking for senior IC or tech-lead roles where I can own the intelligence layer end-to-end.
_Career:_
- Senior Machine Learning Engineer @ Zomato (Food Delivery, 5001-10000, 26mo, current): Built a RAG-based ranking pipeline serving 50M+ queries per month for an internal recruiter-facing search product. The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. Designed the offline evaluation framework from scratch — NDCG, MRR, recall@K calibrated against online A/B engagement metrics. Drove the migration over 4 months including the recruiter-feedback loop that surfaced reranking edge cases.
- Staff Machine Learning Engineer @ Google (Internet, 10001+, 18mo): Built a RAG-based ranking pipeline serving 50M+ queries per month for an internal recruiter-facing search product. The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. Designed the offline evaluation framework from scratch — NDCG, MRR, recall@K calibrated against online A/B engagement metrics. Drove the migration over 4 months including the recruiter-feedback loop that surfaced reranking edge cases.
- Senior Machine Learning Engineer @ Flipkart (E-commerce, 10001+, 42mo): Fine-tuned LLaMA-2-7B and Mistral-7B variants using LoRA and QLoRA for domain-specific candidate-JD matching. Built the data curation pipeline that generated 200K high-quality preference pairs from recruiter labels, plus the eval harness using both ranking metrics and human-quality scores. Deployed the model via BentoML on Kubernetes with sub-200ms p95 latency by quantizing to INT8 and batching at the request level. Cost per inference dropped from $0.04 with GPT-3.5-fallback to under $0.001.
_Edu:_ B.Sc Artificial Intelligence, Massachusetts Institute of Technology (tier_1)
_Edu:_ M.S. Data Science, NIT Surathkal (tier_1)
_Signals:_ last_active 2026-05-13, response_rate 0.61, open_to_work True, notice 15d, relocate True, interview_completion 0.8, github 94.8

`tier: ___`  notes: 


---

**model rank #11**

### CAND_0039383  [submission_top]
**Applied ML Engineer** @ Meesho (E-commerce, 1001-5000) | 7.1y | Gurgaon, Haryana, India
_Summary:_ Machine learning engineer with 7.1 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I built our semantic search infrastructure from scratch — sentence-transformers, FAISS, the works. I've learned that most retrieval problems are actually evaluation problems in disguise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Applied ML Engineer @ Meesho (E-commerce, 1001-5000, 34mo, current): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
- Machine Learning Engineer @ Swiggy (Food Delivery, 5001-10000, 13mo): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
- NLP Engineer @ Paytm (Fintech, 10001+, 37mo): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
_Edu:_ B.Sc Artificial Intelligence, IISc Bangalore (tier_1)
_Signals:_ last_active 2026-03-19, response_rate 0.61, open_to_work True, notice 90d, relocate True, interview_completion 0.97, github 86.4

`tier: ___`  notes: 


---

**model rank #12**

### CAND_0010685  [submission_top]
**NLP Engineer** @ Rephrase.ai (AI/ML, 11-50) | 6.7y | Kolkata, West Bengal, India
_Summary:_ Machine learning engineer with 6.7 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I built our semantic search infrastructure from scratch — sentence-transformers, FAISS, the works. I've spent enough time debugging production ranking issues to know which signals matter and which are noise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- NLP Engineer @ Rephrase.ai (AI/ML, 11-50, 18mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- NLP Engineer @ Microsoft (Software, 10001+, 28mo): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
- Machine Learning Engineer @ Mad Street Den (AI/ML, 201-500, 12mo): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
- Search Engineer @ Mad Street Den (AI/ML, 201-500, 21mo): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
_Edu:_ B.Tech Data Science, Christ University (tier_3)
_Signals:_ last_active 2026-03-16, response_rate 0.83, open_to_work True, notice 30d, relocate False, interview_completion 0.89, github -1

`tier: ___`  notes: 


---

**model rank #13**

### CAND_0046525  [submission_top]
**Senior Machine Learning Engineer** @ Genpact AI (AI Services, 10001+) | 6.1y | Pune, Maharashtra, India
_Summary:_ Senior AI engineer with 6.1 years of hands-on experience building production ML systems, with a focus on search, retrieval, and ranking. Most recently, I designed the company's first hybrid retrieval system combining BM25 with dense vector recall, handling peak QPS of 8K with sub-200ms p95. My day-to-day work spans embedding model selection and fine-tuning, hybrid retrieval architecture, learning-to-rank, behavioral-signal integration, and the offline/online evaluation that ties it all together. I've shipped systems in both early-stage product companies and at larger scale, and I've spent enough time on both that I know which tradeoffs apply where. I care more about shipping a working system in 6 weeks than a theoretically perfect one in 6 months. Currently exploring my next move — looking for senior IC or tech-lead roles where I can own the intelligence layer end-to-end.
_Career:_
- Senior Machine Learning Engineer @ Genpact AI (AI Services, 10001+, 48mo, current): Led the migration from keyword-based to embedding-based search across a 30M+ candidate corpus over 8 months. Designed three successive ranker variants and ran them in A/B testing alongside the legacy keyword system. The final embedding ranker improved recruiter engagement metrics by 24% and reduced the average time-to-shortlist by 38%. Most of the engineering effort went into the boring infrastructure: index versioning, embedding versioning, rollback paths, and the dashboards that let recruiters trust the new system. Mentored two junior engineers through this rollout.
- Senior Machine Learning Engineer @ LinkedIn (Internet, 10001+, 25mo): Built a RAG-based ranking pipeline serving 50M+ queries per month for an internal recruiter-facing search product. The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. Designed the offline evaluation framework from scratch — NDCG, MRR, recall@K calibrated against online A/B engagement metrics. Drove the migration over 4 months including the recruiter-feedback loop that surfaced reranking edge cases.
_Edu:_ M.S. Computer Engineering, Manipal Institute of Technology (tier_2)
_Edu:_ M.Sc Information Technology, IIT Hyderabad (tier_1)
_Signals:_ last_active 2026-05-23, response_rate 0.88, open_to_work True, notice 60d, relocate True, interview_completion 0.81, github 36.7

`tier: ___`  notes: 


---

**model rank #14**

### CAND_0011687  [submission_top]
**Senior NLP Engineer** @ Niramai (HealthTech AI, 51-200) | 7.8y | Indore, Madhya Pradesh, India
_Summary:_ Senior AI engineer with 7.8 years of hands-on experience building production ML systems, with a focus on search, retrieval, and ranking. Most recently, I owned the offline-online evaluation harness — NDCG/MRR/recall calibrated to live A/B metrics, with an index footprint of ~600GB and incremental refresh every 15 min. My day-to-day work spans embedding model selection and fine-tuning, hybrid retrieval architecture, learning-to-rank, behavioral-signal integration, and the offline/online evaluation that ties it all together. I've shipped systems in both early-stage product companies and at larger scale, and I've spent enough time on both that I know which tradeoffs apply where. I believe most ranking problems are solved by careful feature engineering and rigorous eval, not by bigger models. Currently exploring my next move — looking for senior IC or tech-lead roles where I can own the intelligence layer end-to-end.
_Career:_
- Senior NLP Engineer @ Niramai (HealthTech AI, 51-200, 52mo, current): Owned the end-to-end ranking pipeline at a recommendations-heavy consumer product: candidate sourcing → embedding generation (using a fine-tuned BGE-large) → Pinecone retrieval → learning-to-rank re-scoring (XGBoost) → behavioral-signal integration. The hardest part wasn't the ML — it was the evaluation: building offline metrics that actually predicted what the recommendation would do to live engagement. After three iterations we landed on a calibration approach using simulated A/B tests that has held up over the last 18 months.
- Senior Machine Learning Engineer @ Krutrim (AI/ML, 201-500, 40mo): Fine-tuned LLaMA-2-7B and Mistral-7B variants using LoRA and QLoRA for domain-specific candidate-JD matching. Built the data curation pipeline that generated 200K high-quality preference pairs from recruiter labels, plus the eval harness using both ranking metrics and human-quality scores. Deployed the model via BentoML on Kubernetes with sub-200ms p95 latency by quantizing to INT8 and batching at the request level. Cost per inference dropped from $0.04 with GPT-3.5-fallback to under $0.001.
_Edu:_ Ph.D Artificial Intelligence, IIT Delhi (tier_1)
_Signals:_ last_active 2026-05-10, response_rate 0.89, open_to_work True, notice 15d, relocate False, interview_completion 0.77, github 76.3

`tier: ___`  notes: 


---

**model rank #15**

### CAND_0011162  [submission_top]
**Recommendation Systems Engineer** @ upGrad (EdTech, 1001-5000) | 5.8y | Coimbatore, Tamil Nadu, India
_Summary:_ Machine learning engineer with 5.8 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. I've spent enough time debugging production ranking issues to know which signals matter and which are noise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Recommendation Systems Engineer @ upGrad (EdTech, 1001-5000, 25mo, current): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
- Recommendation Systems Engineer @ Meesho (E-commerce, 1001-5000, 28mo): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
- Machine Learning Engineer @ Google (Internet, 10001+, 15mo): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
_Edu:_ M.S. Artificial Intelligence, PES University (tier_2)
_Edu:_ M.S. Data Science, IIT Kharagpur (tier_1)
_Signals:_ last_active 2026-05-10, response_rate 0.75, open_to_work True, notice 90d, relocate True, interview_completion 0.66, github 34.3

`tier: ___`  notes: 


---

**model rank #16**

### CAND_0068811  [submission_top]
**Applied ML Engineer** @ Freshworks (SaaS, 5001-10000) | 8.0y | Pune, Maharashtra, India
_Summary:_ Machine learning engineer with 8.0 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. I care a lot about evaluation rigor — too many teams ship models without offline benchmarks they trust. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Applied ML Engineer @ Freshworks (SaaS, 5001-10000, 19mo, current): Built a content recommendation system serving 10M+ users that combined collaborative filtering with content-based ranking. The system uses item-item similarity (via sentence-transformer embeddings) for cold starts and a gradient-boosted model trained on engagement signals for warm users. Most of my time went into the feature pipeline (~200 features) and the A/B testing infrastructure. The launch improved 7-day retention by 6% and time spent per session by 14%.
- AI Engineer @ Yellow.ai (AI/ML, 201-500, 26mo): Implemented a RAG-based customer support chatbot integrated with our existing ticketing system. Built the document ingestion pipeline (chunking, embedding via OpenAI embeddings, storing in Pinecone) and the answer-generation layer (initially GPT-4, then a fine-tuned smaller model for cost control). Designed the evaluation framework with both automatic metrics (BLEU, ROUGE) and human-in-the-loop quality scores. Deployment cut average ticket resolution time by 31% for the supported categories.
- Recommendation Systems Engineer @ Meesho (E-commerce, 1001-5000, 25mo): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- Search Engineer @ Salesforce (Software, 10001+, 25mo): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
_Edu:_ Ph.D Artificial Intelligence, Thapar University (tier_2)
_Edu:_ M.E. Information Technology, SRM Chennai (tier_3)
_Signals:_ last_active 2026-05-21, response_rate 0.42, open_to_work True, notice 30d, relocate True, interview_completion 0.77, github 23.1

`tier: ___`  notes: 


---

**model rank #17**

### CAND_0018549  [submission_top]
**Recommendation Systems Engineer** @ Uber (Transportation, 10001+) | 6.8y | Coimbatore, Tamil Nadu, India
_Summary:_ Machine learning engineer with 6.8 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. I've learned that most retrieval problems are actually evaluation problems in disguise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Recommendation Systems Engineer @ Uber (Transportation, 10001+, 37mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- Machine Learning Engineer @ Flipkart (E-commerce, 10001+, 44mo): Built a content recommendation system serving 10M+ users that combined collaborative filtering with content-based ranking. The system uses item-item similarity (via sentence-transformer embeddings) for cold starts and a gradient-boosted model trained on engagement signals for warm users. Most of my time went into the feature pipeline (~200 features) and the A/B testing infrastructure. The launch improved 7-day retention by 6% and time spent per session by 14%.
_Edu:_ M.Tech Data Science, Stanford University (tier_1)
_Signals:_ last_active 2026-04-28, response_rate 0.73, open_to_work True, notice 60d, relocate True, interview_completion 0.67, github 56.3

`tier: ___`  notes: 


---

**model rank #18**

### CAND_0062247  [submission_top]
**AI Engineer** @ Google (Internet, 10001+) | 7.3y | Kochi, Kerala, India
_Summary:_ Machine learning engineer with 7.3 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. I've spent enough time debugging production ranking issues to know which signals matter and which are noise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- AI Engineer @ Google (Internet, 10001+, 37mo, current): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
- NLP Engineer @ Dream11 (Gaming, 1001-5000, 50mo): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
_Edu:_ M.E. Machine Learning, IIT Bombay (tier_1)
_Edu:_ B.Sc Information Technology, COEP Pune (tier_2)
_Signals:_ last_active 2026-04-23, response_rate 0.78, open_to_work True, notice 30d, relocate True, interview_completion 0.84, github 52.7

`tier: ___`  notes: 


---

**model rank #19**

### CAND_0088025  [submission_top]
**Staff Machine Learning Engineer** @ Yellow.ai (AI/ML, 201-500) | 8.6y | Jaipur, Rajasthan, India
_Summary:_ Senior AI engineer with 8.6 years of hands-on experience building production ML systems, with a focus on search, retrieval, and ranking. Most recently, I designed the company's first hybrid retrieval system combining BM25 with dense vector recall, serving 50M+ queries per month. My day-to-day work spans embedding model selection and fine-tuning, hybrid retrieval architecture, learning-to-rank, behavioral-signal integration, and the offline/online evaluation that ties it all together. I've shipped systems in both early-stage product companies and at larger scale, and I've spent enough time on both that I know which tradeoffs apply where. I'm comfortable across the stack from infra to algorithms, but my heart is in retrieval and ranking. Currently exploring my next move — looking for senior IC or tech-lead roles where I can own the intelligence layer end-to-end.
_Career:_
- Staff Machine Learning Engineer @ Yellow.ai (AI/ML, 201-500, 45mo, current): Owned the end-to-end ranking pipeline at a recommendations-heavy consumer product: candidate sourcing → embedding generation (using a fine-tuned BGE-large) → Pinecone retrieval → learning-to-rank re-scoring (XGBoost) → behavioral-signal integration. The hardest part wasn't the ML — it was the evaluation: building offline metrics that actually predicted what the recommendation would do to live engagement. After three iterations we landed on a calibration approach using simulated A/B tests that has held up over the last 18 months.
- Staff Machine Learning Engineer @ Niramai (HealthTech AI, 51-200, 44mo): Owned the end-to-end ranking pipeline at a recommendations-heavy consumer product: candidate sourcing → embedding generation (using a fine-tuned BGE-large) → Pinecone retrieval → learning-to-rank re-scoring (XGBoost) → behavioral-signal integration. The hardest part wasn't the ML — it was the evaluation: building offline metrics that actually predicted what the recommendation would do to live engagement. After three iterations we landed on a calibration approach using simulated A/B tests that has held up over the last 18 months.
- Senior Machine Learning Engineer @ Genpact AI (AI Services, 10001+, 13mo): Led the migration from keyword-based to embedding-based search across a 30M+ candidate corpus over 8 months. Designed three successive ranker variants and ran them in A/B testing alongside the legacy keyword system. The final embedding ranker improved recruiter engagement metrics by 24% and reduced the average time-to-shortlist by 38%. Most of the engineering effort went into the boring infrastructure: index versioning, embedding versioning, rollback paths, and the dashboards that let recruiters trust the new system. Mentored two junior engineers through this rollout.
_Edu:_ Ph.D Data Science, COEP Pune (tier_2)
_Signals:_ last_active 2026-05-14, response_rate 0.83, open_to_work True, notice 90d, relocate False, interview_completion 0.95, github 74.6

`tier: ___`  notes: 


---

**model rank #20**

### CAND_0002025  [submission_top]
**Senior AI Engineer** @ Apple (Consumer Electronics, 10001+) | 5.9y | Trivandrum, Kerala, India
_Summary:_ Senior AI engineer with 5.9 years of hands-on experience building production ML systems, with a focus on search, retrieval, and ranking. Most recently, I designed the company's first hybrid retrieval system combining BM25 with dense vector recall, across a corpus of 30M+ candidate profiles. My day-to-day work spans embedding model selection and fine-tuning, hybrid retrieval architecture, learning-to-rank, behavioral-signal integration, and the offline/online evaluation that ties it all together. I've shipped systems in both early-stage product companies and at larger scale, and I've spent enough time on both that I know which tradeoffs apply where. I care more about shipping a working system in 6 weeks than a theoretically perfect one in 6 months. Currently exploring my next move — looking for senior IC or tech-lead roles where I can own the intelligence layer end-to-end.
_Career:_
- Senior AI Engineer @ Apple (Consumer Electronics, 10001+, 42mo, current): Built and shipped a production recommendation system at a marketplace product, going from offline experimentation to live A/B test in 5 months. The system combined collaborative filtering (matrix factorization), content-based features (TF-IDF + sentence-transformer embeddings), and a behavioral re-ranking layer. The most interesting technical challenge was the cold-start problem for new users; I designed an exploration-exploitation policy using Thompson sampling that improved new-user retention by 11% in the first month.
- Lead AI Engineer @ Aganitha (AI/ML, 51-200, 28mo): Fine-tuned LLaMA-2-7B and Mistral-7B variants using LoRA and QLoRA for domain-specific candidate-JD matching. Built the data curation pipeline that generated 200K high-quality preference pairs from recruiter labels, plus the eval harness using both ranking metrics and human-quality scores. Deployed the model via BentoML on Kubernetes with sub-200ms p95 latency by quantizing to INT8 and batching at the request level. Cost per inference dropped from $0.04 with GPT-3.5-fallback to under $0.001.
_Edu:_ M.Sc Data Science, IIIT Bangalore (tier_1)
_Edu:_ M.S. Data Science, IIIT Bangalore (tier_1)
_Signals:_ last_active 2026-05-26, response_rate 0.8, open_to_work True, notice 30d, relocate False, interview_completion 0.81, github 96.9

`tier: ___`  notes: 


---

**model rank #21**

### CAND_0074225  [submission_top]
**Machine Learning Engineer** @ Unacademy (EdTech, 5001-10000) | 4.3y | Vizag, Andhra Pradesh, India
_Summary:_ Machine learning engineer with 4.3 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, my main project for the last 18 months has been the recommendation system that powers our discovery feed. I've learned that most retrieval problems are actually evaluation problems in disguise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Machine Learning Engineer @ Unacademy (EdTech, 5001-10000, 26mo, current): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
- Machine Learning Engineer @ Mad Street Den (AI/ML, 201-500, 25mo): Implemented a RAG-based customer support chatbot integrated with our existing ticketing system. Built the document ingestion pipeline (chunking, embedding via OpenAI embeddings, storing in Pinecone) and the answer-generation layer (initially GPT-4, then a fine-tuned smaller model for cost control). Designed the evaluation framework with both automatic metrics (BLEU, ROUGE) and human-in-the-loop quality scores. Deployment cut average ticket resolution time by 31% for the supported categories.
_Edu:_ M.S. Computer Engineering, Thapar University (tier_2)
_Signals:_ last_active 2026-05-20, response_rate 0.91, open_to_work True, notice 120d, relocate True, interview_completion 0.8, github 54.3

`tier: ___`  notes: 


---

**model rank #22**

### CAND_0057563  [submission_top]
**NLP Engineer** @ Locobuzz (AI/ML, 51-200) | 6.8y | Indore, Madhya Pradesh, India
_Summary:_ Machine learning engineer with 6.8 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I built our semantic search infrastructure from scratch — sentence-transformers, FAISS, the works. I've learned that most retrieval problems are actually evaluation problems in disguise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- NLP Engineer @ Locobuzz (AI/ML, 51-200, 20mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- Machine Learning Engineer @ Yellow.ai (AI/ML, 201-500, 34mo): Built a content recommendation system serving 10M+ users that combined collaborative filtering with content-based ranking. The system uses item-item similarity (via sentence-transformer embeddings) for cold starts and a gradient-boosted model trained on engagement signals for warm users. Most of my time went into the feature pipeline (~200 features) and the A/B testing infrastructure. The launch improved 7-day retention by 6% and time spent per session by 14%.
- Senior Data Scientist @ Zoho (SaaS, 10001+, 26mo): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
_Edu:_ M.E. Computer Science, BITS Pilani (tier_1)
_Edu:_ B.E. Information Technology, Amity University (tier_3)
_Signals:_ last_active 2026-04-21, response_rate 0.83, open_to_work False, notice 60d, relocate True, interview_completion 0.81, github 22.8

`tier: ___`  notes: 


---

**model rank #23**

### CAND_0060054  [submission_top]
**AI Engineer** @ Mad Street Den (AI/ML, 201-500) | 6.4y | Jaipur, Rajasthan, India
_Summary:_ Machine learning engineer with 6.4 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, my main project for the last 18 months has been the recommendation system that powers our discovery feed. I care a lot about evaluation rigor — too many teams ship models without offline benchmarks they trust. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- AI Engineer @ Mad Street Den (AI/ML, 201-500, 31mo, current): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
- Recommendation Systems Engineer @ Zomato (Food Delivery, 5001-10000, 24mo): Built a content recommendation system serving 10M+ users that combined collaborative filtering with content-based ranking. The system uses item-item similarity (via sentence-transformer embeddings) for cold starts and a gradient-boosted model trained on engagement signals for warm users. Most of my time went into the feature pipeline (~200 features) and the A/B testing infrastructure. The launch improved 7-day retention by 6% and time spent per session by 14%.
- AI Engineer @ Uber (Transportation, 10001+, 21mo): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
_Edu:_ Ph.D Data Science, RV College of Engineering (tier_2)
_Signals:_ last_active 2026-03-17, response_rate 0.86, open_to_work False, notice 15d, relocate True, interview_completion 0.78, github -1

`tier: ___`  notes: 


---

**model rank #24**

### CAND_0018722  [submission_top]
**Recommendation Systems Engineer** @ Saarthi.ai (Voice AI, 11-50) | 6.6y | Toronto, Canada
_Summary:_ Machine learning engineer with 6.6 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. Along the way I've gotten comfortable with the operational side — A/B testing, drift monitoring, retraining schedules. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Recommendation Systems Engineer @ Saarthi.ai (Voice AI, 11-50, 28mo, current): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
- Machine Learning Engineer @ Unacademy (EdTech, 5001-10000, 30mo): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- Applied ML Engineer @ Swiggy (Food Delivery, 5001-10000, 20mo): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
_Edu:_ B.Tech Artificial Intelligence, Manipal Institute of Technology (tier_2)
_Signals:_ last_active 2026-04-24, response_rate 0.79, open_to_work True, notice 90d, relocate True, interview_completion 0.91, github 94.3

`tier: ___`  notes: 


---

**model rank #25**

### CAND_0017960  [submission_top]
**Recommendation Systems Engineer** @ Nykaa (E-commerce, 1001-5000) | 7.7y | Bangalore, Karnataka, India
_Summary:_ Machine learning engineer with 7.7 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I built our semantic search infrastructure from scratch — sentence-transformers, FAISS, the works. Along the way I've gotten comfortable with the operational side — A/B testing, drift monitoring, retraining schedules. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Recommendation Systems Engineer @ Nykaa (E-commerce, 1001-5000, 54mo, current): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
- NLP Engineer @ Wysa (HealthTech AI, 51-200, 21mo): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
- Search Engineer @ Sarvam AI (AI/ML, 51-200, 16mo): Implemented a RAG-based customer support chatbot integrated with our existing ticketing system. Built the document ingestion pipeline (chunking, embedding via OpenAI embeddings, storing in Pinecone) and the answer-generation layer (initially GPT-4, then a fine-tuned smaller model for cost control). Designed the evaluation framework with both automatic metrics (BLEU, ROUGE) and human-in-the-loop quality scores. Deployment cut average ticket resolution time by 31% for the supported categories.
_Edu:_ B.Sc Information Technology, IIT Delhi (tier_1)
_Signals:_ last_active 2026-04-27, response_rate 0.72, open_to_work True, notice 60d, relocate True, interview_completion 0.64, github 92.4

`tier: ___`  notes: 


---

**model rank #26**

### CAND_0011432  [submission_top]
**Senior Data Scientist** @ Amazon (Internet, 10001+) | 7.6y | Chennai, Tamil Nadu, India
_Summary:_ Machine learning engineer with 7.6 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I've been the de-facto ML lead on a small team, shipping models across NLP and recsys. I've learned that most retrieval problems are actually evaluation problems in disguise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Senior Data Scientist @ Amazon (Internet, 10001+, 28mo, current): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
- Machine Learning Engineer @ Krutrim (AI/ML, 201-500, 36mo): Implemented a RAG-based customer support chatbot integrated with our existing ticketing system. Built the document ingestion pipeline (chunking, embedding via OpenAI embeddings, storing in Pinecone) and the answer-generation layer (initially GPT-4, then a fine-tuned smaller model for cost control). Designed the evaluation framework with both automatic metrics (BLEU, ROUGE) and human-in-the-loop quality scores. Deployment cut average ticket resolution time by 31% for the supported categories.
- NLP Engineer @ Nykaa (E-commerce, 1001-5000, 26mo): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
_Edu:_ M.Sc Data Science, Bharati Vidyapeeth (tier_3)
_Signals:_ last_active 2026-03-16, response_rate 0.67, open_to_work True, notice 60d, relocate False, interview_completion 0.83, github 20.0

`tier: ___`  notes: 


---

**model rank #27**

### CAND_0043228  [submission_top]
**Applied ML Engineer** @ Zoho (SaaS, 10001+) | 6.8y | Chennai, Tamil Nadu, India
_Summary:_ Machine learning engineer with 6.8 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I built our semantic search infrastructure from scratch — sentence-transformers, FAISS, the works. I've learned that most retrieval problems are actually evaluation problems in disguise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Applied ML Engineer @ Zoho (SaaS, 10001+, 25mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- Applied ML Engineer @ Vedantu (EdTech, 1001-5000, 44mo): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
- Search Engineer @ Yellow.ai (AI/ML, 201-500, 11mo): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
_Edu:_ B.E. Artificial Intelligence, IIT Madras (tier_1)
_Signals:_ last_active 2026-05-22, response_rate 0.41, open_to_work False, notice 30d, relocate False, interview_completion 0.94, github 47.6

`tier: ___`  notes: 


---

**model rank #28**

### CAND_0078492  [submission_top]
**Recommendation Systems Engineer** @ Verloop.io (Conversational AI, 51-200) | 5.1y | Kochi, Kerala, India
_Summary:_ Machine learning engineer with 5.1 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I built our semantic search infrastructure from scratch — sentence-transformers, FAISS, the works. I've spent enough time debugging production ranking issues to know which signals matter and which are noise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Recommendation Systems Engineer @ Verloop.io (Conversational AI, 51-200, 12mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- Senior Data Scientist @ Adobe (Software, 10001+, 49mo): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
_Edu:_ B.E. Computer Engineering, IIT Delhi (tier_1)
_Signals:_ last_active 2026-04-01, response_rate 0.7, open_to_work True, notice 30d, relocate True, interview_completion 0.89, github 35.4

`tier: ___`  notes: 


---

**model rank #29**

### CAND_0042029  [submission_top]
**Senior Data Scientist** @ Flipkart (E-commerce, 10001+) | 6.5y | Delhi, Delhi, India
_Summary:_ Machine learning engineer with 6.5 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I built our semantic search infrastructure from scratch — sentence-transformers, FAISS, the works. I care a lot about evaluation rigor — too many teams ship models without offline benchmarks they trust. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Senior Data Scientist @ Flipkart (E-commerce, 10001+, 36mo, current): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
- Machine Learning Engineer @ Observe.AI (AI/ML, 201-500, 42mo): Implemented a RAG-based customer support chatbot integrated with our existing ticketing system. Built the document ingestion pipeline (chunking, embedding via OpenAI embeddings, storing in Pinecone) and the answer-generation layer (initially GPT-4, then a fine-tuned smaller model for cost control). Designed the evaluation framework with both automatic metrics (BLEU, ROUGE) and human-in-the-loop quality scores. Deployment cut average ticket resolution time by 31% for the supported categories.
_Edu:_ B.E. Computer Science, PES University (tier_2)
_Signals:_ last_active 2026-04-13, response_rate 0.67, open_to_work False, notice 45d, relocate True, interview_completion 0.74, github 78.7

`tier: ___`  notes: 


---

**model rank #30**

### CAND_0083879  [submission_top]
**Machine Learning Engineer** @ Ola (Transportation, 5001-10000) | 7.1y | Noida, Uttar Pradesh, India
_Summary:_ Machine learning engineer with 7.1 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I built our semantic search infrastructure from scratch — sentence-transformers, FAISS, the works. I've spent enough time debugging production ranking issues to know which signals matter and which are noise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Machine Learning Engineer @ Ola (Transportation, 5001-10000, 19mo, current): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
- Search Engineer @ PhonePe (Fintech, 5001-10000, 46mo): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
- Senior Data Scientist @ Swiggy (Food Delivery, 5001-10000, 19mo): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
_Edu:_ B.Sc Information Technology, NIT Surathkal (tier_1)
_Signals:_ last_active 2026-04-17, response_rate 0.47, open_to_work True, notice 30d, relocate False, interview_completion 0.83, github -1

`tier: ___`  notes: 


---

**model rank #31**

### CAND_0050876  [submission_top]
**Applied ML Engineer** @ Freshworks (SaaS, 5001-10000) | 6.0y | Kolkata, West Bengal, India
_Summary:_ Machine learning engineer with 6.0 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, my main project for the last 18 months has been the recommendation system that powers our discovery feed. I care a lot about evaluation rigor — too many teams ship models without offline benchmarks they trust. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Applied ML Engineer @ Freshworks (SaaS, 5001-10000, 38mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- AI Engineer @ Yellow.ai (AI/ML, 201-500, 24mo): Built a content recommendation system serving 10M+ users that combined collaborative filtering with content-based ranking. The system uses item-item similarity (via sentence-transformer embeddings) for cold starts and a gradient-boosted model trained on engagement signals for warm users. Most of my time went into the feature pipeline (~200 features) and the A/B testing infrastructure. The launch improved 7-day retention by 6% and time spent per session by 14%.
- Recommendation Systems Engineer @ Razorpay (Fintech, 1001-5000, 9mo): Built a content recommendation system serving 10M+ users that combined collaborative filtering with content-based ranking. The system uses item-item similarity (via sentence-transformer embeddings) for cold starts and a gradient-boosted model trained on engagement signals for warm users. Most of my time went into the feature pipeline (~200 features) and the A/B testing infrastructure. The launch improved 7-day retention by 6% and time spent per session by 14%.
_Edu:_ M.S. Machine Learning, Stanford University (tier_1)
_Edu:_ M.E. Information Technology, IIT Kharagpur (tier_1)
_Signals:_ last_active 2026-05-26, response_rate 0.67, open_to_work True, notice 90d, relocate False, interview_completion 0.97, github 86.1

`tier: ___`  notes: 


---

**model rank #32**

### CAND_0093912  [submission_top]
**Senior Data Scientist** @ Razorpay (Fintech, 1001-5000) | 5.3y | Chandigarh, Chandigarh, India
_Summary:_ Machine learning engineer with 5.3 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I shipped our first RAG-based feature this year and now own the eval framework for it. I care a lot about evaluation rigor — too many teams ship models without offline benchmarks they trust. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Senior Data Scientist @ Razorpay (Fintech, 1001-5000, 27mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- Search Engineer @ Flipkart (E-commerce, 10001+, 19mo): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
- AI Engineer @ Apple (Consumer Electronics, 10001+, 16mo): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
_Edu:_ B.Sc Computer Science, RV College of Engineering (tier_2)
_Signals:_ last_active 2026-05-11, response_rate 0.66, open_to_work True, notice 30d, relocate False, interview_completion 0.96, github 81.5

`tier: ___`  notes: 


---

**model rank #33**

### CAND_0008425  [submission_top]
**Senior NLP Engineer** @ Ola (Transportation, 5001-10000) | 7.8y | Kolkata, West Bengal, India
_Summary:_ Senior AI engineer with 7.8 years of hands-on experience building production ML systems, with a focus on search, retrieval, and ranking. Most recently, I rebuilt the candidate-JD matching pipeline from scratch, taking it from 0.72 to 0.91 NDCG@10, operating at single-digit-millisecond p95 retrieval latency. My day-to-day work spans embedding model selection and fine-tuning, hybrid retrieval architecture, learning-to-rank, behavioral-signal integration, and the offline/online evaluation that ties it all together. I've shipped systems in both early-stage product companies and at larger scale, and I've spent enough time on both that I know which tradeoffs apply where. I've made all the standard mistakes — embedding everything before defining the metric, over-investing in fine-tuning, optimizing offline metrics that don't move online — so I notice them faster now. Currently exploring my next move — looking for senior IC or tech-lead roles where I can own the intelligence layer end-to-end.
_Career:_
- Senior NLP Engineer @ Ola (Transportation, 5001-10000, 25mo, current): Owned the design and rollout of a large-scale semantic search system serving an internal corpus of 35M+ items. Migrated the existing BM25-only retrieval to a hybrid setup combining sparse and dense vectors (sentence-transformers, MPNet-base initially, later fine-tuned BGE-large for our domain). The new system reduced p95 retrieval latency by 60% while improving NDCG@10 by 18% on our held-out eval set. Spent substantial time on the boring-but-critical parts: incremental index refresh, embedding drift monitoring, online/offline metric correlation. Led a team of 4 engineers across the rollout.
- Senior ML Engineer — Search & Ranking @ Zomato (Food Delivery, 5001-10000, 46mo): Fine-tuned LLaMA-2-7B and Mistral-7B variants using LoRA and QLoRA for domain-specific candidate-JD matching. Built the data curation pipeline that generated 200K high-quality preference pairs from recruiter labels, plus the eval harness using both ranking metrics and human-quality scores. Deployed the model via BentoML on Kubernetes with sub-200ms p95 latency by quantizing to INT8 and batching at the request level. Cost per inference dropped from $0.04 with GPT-3.5-fallback to under $0.001.
- Lead AI Engineer @ Amazon (Internet, 10001+, 21mo): Owned the end-to-end ranking pipeline at a recommendations-heavy consumer product: candidate sourcing → embedding generation (using a fine-tuned BGE-large) → Pinecone retrieval → learning-to-rank re-scoring (XGBoost) → behavioral-signal integration. The hardest part wasn't the ML — it was the evaluation: building offline metrics that actually predicted what the recommendation would do to live engagement. After three iterations we landed on a calibration approach using simulated A/B tests that has held up over the last 18 months.
_Edu:_ M.S. Computer Engineering, BITS Pilani (tier_1)
_Signals:_ last_active 2026-04-25, response_rate 0.66, open_to_work True, notice 90d, relocate False, interview_completion 0.77, github 53.3

`tier: ___`  notes: 


---

**model rank #34**

### CAND_0071974  [submission_top]
**Senior AI Engineer** @ Netflix (Media, 10001+) | 7.8y | Vizag, Andhra Pradesh, India
_Summary:_ Senior AI engineer with 7.8 years of hands-on experience building production ML systems, with a focus on search, retrieval, and ranking. Most recently, I led the migration from keyword-based ranking to a learning-to-rank model with embedded behavioral signals, handling peak QPS of 8K with sub-200ms p95. My day-to-day work spans embedding model selection and fine-tuning, hybrid retrieval architecture, learning-to-rank, behavioral-signal integration, and the offline/online evaluation that ties it all together. I've shipped systems in both early-stage product companies and at larger scale, and I've spent enough time on both that I know which tradeoffs apply where. I believe most ranking problems are solved by careful feature engineering and rigorous eval, not by bigger models. Currently exploring my next move — looking for senior IC or tech-lead roles where I can own the intelligence layer end-to-end.
_Career:_
- Senior AI Engineer @ Netflix (Media, 10001+, 50mo, current): Owned the end-to-end ranking pipeline at a recommendations-heavy consumer product: candidate sourcing → embedding generation (using a fine-tuned BGE-large) → Pinecone retrieval → learning-to-rank re-scoring (XGBoost) → behavioral-signal integration. The hardest part wasn't the ML — it was the evaluation: building offline metrics that actually predicted what the recommendation would do to live engagement. After three iterations we landed on a calibration approach using simulated A/B tests that has held up over the last 18 months.
- Staff Machine Learning Engineer @ Meta (Internet, 10001+, 28mo): Fine-tuned LLaMA-2-7B and Mistral-7B variants using LoRA and QLoRA for domain-specific candidate-JD matching. Built the data curation pipeline that generated 200K high-quality preference pairs from recruiter labels, plus the eval harness using both ranking metrics and human-quality scores. Deployed the model via BentoML on Kubernetes with sub-200ms p95 latency by quantizing to INT8 and batching at the request level. Cost per inference dropped from $0.04 with GPT-3.5-fallback to under $0.001.
- Staff Machine Learning Engineer @ Mad Street Den (AI/ML, 201-500, 14mo): Built and shipped a production recommendation system at a marketplace product, going from offline experimentation to live A/B test in 5 months. The system combined collaborative filtering (matrix factorization), content-based features (TF-IDF + sentence-transformer embeddings), and a behavioral re-ranking layer. The most interesting technical challenge was the cold-start problem for new users; I designed an exploration-exploitation policy using Thompson sampling that improved new-user retention by 11% in the first month.
_Edu:_ M.Sc Artificial Intelligence, NIT Warangal (tier_1)
_Signals:_ last_active 2026-04-16, response_rate 0.76, open_to_work True, notice 45d, relocate False, interview_completion 0.85, github 82.8

`tier: ___`  notes: 


---

**model rank #35**

### CAND_0027691  [submission_top]
**NLP Engineer** @ Haptik (Conversational AI, 201-500) | 6.5y | Pune, Maharashtra, India
_Summary:_ Machine learning engineer with 6.5 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, my main project for the last 18 months has been the recommendation system that powers our discovery feed. Along the way I've gotten comfortable with the operational side — A/B testing, drift monitoring, retraining schedules. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- NLP Engineer @ Haptik (Conversational AI, 201-500, 27mo, current): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
- Applied ML Engineer @ Vedantu (EdTech, 1001-5000, 33mo): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
- AI Engineer @ Meta (Internet, 10001+, 16mo): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
_Edu:_ M.Sc Machine Learning, Thapar University (tier_2)
_Edu:_ M.E. Data Science, KIIT University (tier_3)
_Signals:_ last_active 2026-03-31, response_rate 0.68, open_to_work True, notice 15d, relocate False, interview_completion 0.63, github 58.5

`tier: ___`  notes: 


---

**model rank #36**

### CAND_0031593  [submission_top]
**Search Engineer** @ Genpact AI (AI Services, 10001+) | 7.8y | Kolkata, West Bengal, India
_Summary:_ Machine learning engineer with 7.8 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, my main project for the last 18 months has been the recommendation system that powers our discovery feed. I've learned that most retrieval problems are actually evaluation problems in disguise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Search Engineer @ Genpact AI (AI Services, 10001+, 38mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- NLP Engineer @ Unacademy (EdTech, 5001-10000, 21mo): Implemented a RAG-based customer support chatbot integrated with our existing ticketing system. Built the document ingestion pipeline (chunking, embedding via OpenAI embeddings, storing in Pinecone) and the answer-generation layer (initially GPT-4, then a fine-tuned smaller model for cost control). Designed the evaluation framework with both automatic metrics (BLEU, ROUGE) and human-in-the-loop quality scores. Deployment cut average ticket resolution time by 31% for the supported categories.
- Search Engineer @ Aganitha (AI/ML, 51-200, 33mo): Built a content recommendation system serving 10M+ users that combined collaborative filtering with content-based ranking. The system uses item-item similarity (via sentence-transformer embeddings) for cold starts and a gradient-boosted model trained on engagement signals for warm users. Most of my time went into the feature pipeline (~200 features) and the A/B testing infrastructure. The launch improved 7-day retention by 6% and time spent per session by 14%.
_Edu:_ Ph.D Information Technology, SRM University (tier_2)
_Signals:_ last_active 2026-03-19, response_rate 0.58, open_to_work True, notice 90d, relocate True, interview_completion 0.79, github 23.2

`tier: ___`  notes: 


---

**model rank #37**

### CAND_0019480  [submission_top]
**NLP Engineer** @ Meesho (E-commerce, 1001-5000) | 2.8y | Chennai, Tamil Nadu, India
_Summary:_ Machine learning engineer with 7.4 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. I care a lot about evaluation rigor — too many teams ship models without offline benchmarks they trust. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- NLP Engineer @ Meesho (E-commerce, 1001-5000, 19mo, current): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
- Senior Data Scientist @ InMobi (AdTech, 1001-5000, 26mo): Implemented a RAG-based customer support chatbot integrated with our existing ticketing system. Built the document ingestion pipeline (chunking, embedding via OpenAI embeddings, storing in Pinecone) and the answer-generation layer (initially GPT-4, then a fine-tuned smaller model for cost control). Designed the evaluation framework with both automatic metrics (BLEU, ROUGE) and human-in-the-loop quality scores. Deployment cut average ticket resolution time by 31% for the supported categories.
- Senior Data Scientist @ Vedantu (EdTech, 1001-5000, 27mo): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
- Search Engineer @ Freshworks (SaaS, 5001-10000, 15mo): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
_Edu:_ B.Tech Machine Learning, Thapar University (tier_2)
_Signals:_ last_active 2026-05-13, response_rate 0.87, open_to_work True, notice 90d, relocate True, interview_completion 0.84, github 69.8

`tier: ___`  notes: 


---

**model rank #38**

### CAND_0049538  [submission_top]
**Applied ML Engineer** @ Saarthi.ai (Voice AI, 11-50) | 5.8y | Jaipur, Rajasthan, India
_Summary:_ Machine learning engineer with 5.8 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. I've spent enough time debugging production ranking issues to know which signals matter and which are noise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Applied ML Engineer @ Saarthi.ai (Voice AI, 11-50, 40mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- Recommendation Systems Engineer @ PolicyBazaar (Insurance Tech, 5001-10000, 19mo): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
- AI Engineer @ Zoho (SaaS, 10001+, 9mo): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
_Edu:_ B.E. Data Science, NIT Warangal (tier_1)
_Signals:_ last_active 2026-05-27, response_rate 0.72, open_to_work False, notice 30d, relocate False, interview_completion 0.67, github 90.8

`tier: ___`  notes: 


---

**model rank #39**

### CAND_0079387  [submission_top]
**AI Engineer** @ Microsoft (Software, 10001+) | 6.9y | Trivandrum, Kerala, India
_Summary:_ Machine learning engineer with 6.9 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I've been the de-facto ML lead on a small team, shipping models across NLP and recsys. I've learned that most retrieval problems are actually evaluation problems in disguise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- AI Engineer @ Microsoft (Software, 10001+, 22mo, current): Built a content recommendation system serving 10M+ users that combined collaborative filtering with content-based ranking. The system uses item-item similarity (via sentence-transformer embeddings) for cold starts and a gradient-boosted model trained on engagement signals for warm users. Most of my time went into the feature pipeline (~200 features) and the A/B testing infrastructure. The launch improved 7-day retention by 6% and time spent per session by 14%.
- NLP Engineer @ upGrad (EdTech, 1001-5000, 22mo): Implemented a RAG-based customer support chatbot integrated with our existing ticketing system. Built the document ingestion pipeline (chunking, embedding via OpenAI embeddings, storing in Pinecone) and the answer-generation layer (initially GPT-4, then a fine-tuned smaller model for cost control). Designed the evaluation framework with both automatic metrics (BLEU, ROUGE) and human-in-the-loop quality scores. Deployment cut average ticket resolution time by 31% for the supported categories.
- Applied ML Engineer @ Ola (Transportation, 5001-10000, 18mo): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
- AI Engineer @ BYJU'S (EdTech, 10001+, 19mo): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
_Edu:_ M.Sc Computer Science, IIIT Hyderabad (tier_1)
_Edu:_ B.E. Data Science, PES University (tier_2)
_Signals:_ last_active 2026-04-25, response_rate 0.81, open_to_work True, notice 30d, relocate False, interview_completion 0.9, github 64.1

`tier: ___`  notes: 


---

**model rank #40**

### CAND_0005260  [submission_top]
**Senior NLP Engineer** @ Netflix (Media, 10001+) | 5.2y | Chennai, Tamil Nadu, India
_Summary:_ Senior AI engineer with 5.2 years of hands-on experience building production ML systems, with a focus on search, retrieval, and ranking. Most recently, I drove the platform's RAG strategy from prototype to production, including the eval framework, operating at single-digit-millisecond p95 retrieval latency. My day-to-day work spans embedding model selection and fine-tuning, hybrid retrieval architecture, learning-to-rank, behavioral-signal integration, and the offline/online evaluation that ties it all together. I've shipped systems in both early-stage product companies and at larger scale, and I've spent enough time on both that I know which tradeoffs apply where. I believe most ranking problems are solved by careful feature engineering and rigorous eval, not by bigger models. Currently exploring my next move — looking for senior IC or tech-lead roles where I can own the intelligence layer end-to-end.
_Career:_
- Senior NLP Engineer @ Netflix (Media, 10001+, 34mo, current): Fine-tuned LLaMA-2-7B and Mistral-7B variants using LoRA and QLoRA for domain-specific candidate-JD matching. Built the data curation pipeline that generated 200K high-quality preference pairs from recruiter labels, plus the eval harness using both ranking metrics and human-quality scores. Deployed the model via BentoML on Kubernetes with sub-200ms p95 latency by quantizing to INT8 and batching at the request level. Cost per inference dropped from $0.04 with GPT-3.5-fallback to under $0.001.
- Senior NLP Engineer @ Yellow.ai (AI/ML, 201-500, 27mo): Built a RAG-based ranking pipeline serving 50M+ queries per month for an internal recruiter-facing search product. The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. Designed the offline evaluation framework from scratch — NDCG, MRR, recall@K calibrated against online A/B engagement metrics. Drove the migration over 4 months including the recruiter-feedback loop that surfaced reranking edge cases.
_Edu:_ B.Tech Artificial Intelligence, IIIT Bangalore (tier_1)
_Signals:_ last_active 2026-05-10, response_rate 0.86, open_to_work False, notice 60d, relocate True, interview_completion 0.73, github -1

`tier: ___`  notes: 


---

**model rank #41**

### CAND_0086022  [submission_top]
**Senior Applied Scientist** @ Sarvam AI (AI/ML, 51-200) | 5.3y | Kolkata, West Bengal, India
_Summary:_ Senior AI engineer with 5.3 years of hands-on experience building production ML systems, with a focus on search, retrieval, and ranking. Most recently, I led the migration from keyword-based ranking to a learning-to-rank model with embedded behavioral signals, handling peak QPS of 8K with sub-200ms p95. My day-to-day work spans embedding model selection and fine-tuning, hybrid retrieval architecture, learning-to-rank, behavioral-signal integration, and the offline/online evaluation that ties it all together. I've shipped systems in both early-stage product companies and at larger scale, and I've spent enough time on both that I know which tradeoffs apply where. I've made all the standard mistakes — embedding everything before defining the metric, over-investing in fine-tuning, optimizing offline metrics that don't move online — so I notice them faster now. Currently exploring my next move — looking for senior IC or tech-lead roles where I can own the intelligence layer end-to-end.
_Career:_
- Senior Applied Scientist @ Sarvam AI (AI/ML, 51-200, 25mo, current): Built a RAG-based ranking pipeline serving 50M+ queries per month for an internal recruiter-facing search product. The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. Designed the offline evaluation framework from scratch — NDCG, MRR, recall@K calibrated against online A/B engagement metrics. Drove the migration over 4 months including the recruiter-feedback loop that surfaced reranking edge cases.
- Senior ML Engineer — Search & Ranking @ Uber (Transportation, 10001+, 38mo): Led the migration from keyword-based to embedding-based search across a 30M+ candidate corpus over 8 months. Designed three successive ranker variants and ran them in A/B testing alongside the legacy keyword system. The final embedding ranker improved recruiter engagement metrics by 24% and reduced the average time-to-shortlist by 38%. Most of the engineering effort went into the boring infrastructure: index versioning, embedding versioning, rollback paths, and the dashboards that let recruiters trust the new system. Mentored two junior engineers through this rollout.
_Edu:_ B.Tech Data Science, Stanford University (tier_1)
_Signals:_ last_active 2026-04-15, response_rate 0.55, open_to_work True, notice 0d, relocate True, interview_completion 0.68, github 75.2

`tier: ___`  notes: 


---

**model rank #42**

### CAND_0036437  [submission_top]
**Search Engineer** @ Rephrase.ai (AI/ML, 11-50) | 4.8y | Kolkata, West Bengal, India
_Summary:_ Machine learning engineer with 4.8 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I shipped our first RAG-based feature this year and now own the eval framework for it. I've spent enough time debugging production ranking issues to know which signals matter and which are noise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Search Engineer @ Rephrase.ai (AI/ML, 11-50, 21mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- Machine Learning Engineer @ Nykaa (E-commerce, 1001-5000, 16mo): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- AI Engineer @ Ola (Transportation, 5001-10000, 19mo): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
_Edu:_ B.Tech Machine Learning, Anna University (tier_2)
_Signals:_ last_active 2026-05-14, response_rate 0.87, open_to_work False, notice 30d, relocate True, interview_completion 0.9, github 35.2

`tier: ___`  notes: 


---

**model rank #43**

### CAND_0098846  [submission_top]
**AI Engineer** @ upGrad (EdTech, 1001-5000) | 7.6y | Indore, Madhya Pradesh, India
_Summary:_ Machine learning engineer with 7.6 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I've been the de-facto ML lead on a small team, shipping models across NLP and recsys. Along the way I've gotten comfortable with the operational side — A/B testing, drift monitoring, retraining schedules. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- AI Engineer @ upGrad (EdTech, 1001-5000, 25mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- Machine Learning Engineer @ Meesho (E-commerce, 1001-5000, 20mo): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
- Search Engineer @ Swiggy (Food Delivery, 5001-10000, 19mo): Implemented a RAG-based customer support chatbot integrated with our existing ticketing system. Built the document ingestion pipeline (chunking, embedding via OpenAI embeddings, storing in Pinecone) and the answer-generation layer (initially GPT-4, then a fine-tuned smaller model for cost control). Designed the evaluation framework with both automatic metrics (BLEU, ROUGE) and human-in-the-loop quality scores. Deployment cut average ticket resolution time by 31% for the supported categories.
- Search Engineer @ Google (Internet, 10001+, 26mo): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
_Edu:_ Ph.D Machine Learning, IIT Kanpur (tier_1)
_Signals:_ last_active 2026-04-23, response_rate 0.62, open_to_work True, notice 45d, relocate True, interview_completion 0.8, github 86.2

`tier: ___`  notes: 


---

**model rank #44**

### CAND_0075574  [submission_top]
**Machine Learning Engineer** @ Haptik (Conversational AI, 201-500) | 5.7y | Bangalore, Karnataka, India
_Summary:_ Machine learning engineer with 5.7 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I shipped our first RAG-based feature this year and now own the eval framework for it. I've spent enough time debugging production ranking issues to know which signals matter and which are noise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Machine Learning Engineer @ Haptik (Conversational AI, 201-500, 24mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- Machine Learning Engineer @ Observe.AI (AI/ML, 201-500, 36mo): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
- NLP Engineer @ Genpact AI (AI Services, 10001+, 8mo): Implemented a RAG-based customer support chatbot integrated with our existing ticketing system. Built the document ingestion pipeline (chunking, embedding via OpenAI embeddings, storing in Pinecone) and the answer-generation layer (initially GPT-4, then a fine-tuned smaller model for cost control). Designed the evaluation framework with both automatic metrics (BLEU, ROUGE) and human-in-the-loop quality scores. Deployment cut average ticket resolution time by 31% for the supported categories.
_Edu:_ M.S. Computer Science, Carnegie Mellon University (tier_1)
_Signals:_ last_active 2026-05-17, response_rate 0.58, open_to_work True, notice 60d, relocate True, interview_completion 0.96, github 37.7

`tier: ___`  notes: 


---

**model rank #45**

### CAND_0005649  [submission_top]
**Senior Data Scientist** @ Sarvam AI (AI/ML, 51-200) | 7.4y | Delhi, Delhi, India
_Summary:_ Machine learning engineer with 7.4 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I built our semantic search infrastructure from scratch — sentence-transformers, FAISS, the works. Along the way I've gotten comfortable with the operational side — A/B testing, drift monitoring, retraining schedules. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Senior Data Scientist @ Sarvam AI (AI/ML, 51-200, 18mo, current): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
- Recommendation Systems Engineer @ Aganitha (AI/ML, 51-200, 12mo): Implemented a RAG-based customer support chatbot integrated with our existing ticketing system. Built the document ingestion pipeline (chunking, embedding via OpenAI embeddings, storing in Pinecone) and the answer-generation layer (initially GPT-4, then a fine-tuned smaller model for cost control). Designed the evaluation framework with both automatic metrics (BLEU, ROUGE) and human-in-the-loop quality scores. Deployment cut average ticket resolution time by 31% for the supported categories.
- Senior Data Scientist @ Amazon (Internet, 10001+, 42mo): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
- Search Engineer @ Glance (AI/ML, 501-1000, 16mo): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
_Edu:_ Ph.D Information Technology, RV College of Engineering (tier_2)
_Signals:_ last_active 2026-04-14, response_rate 0.57, open_to_work True, notice 90d, relocate True, interview_completion 0.88, github 80.7

`tier: ___`  notes: 


---

**model rank #46**

### CAND_0012957  [submission_top]
**Search Engineer** @ Razorpay (Fintech, 1001-5000) | 4.9y | Chennai, Tamil Nadu, India
_Summary:_ Machine learning engineer with 4.9 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. I've learned that most retrieval problems are actually evaluation problems in disguise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Search Engineer @ Razorpay (Fintech, 1001-5000, 18mo, current): Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%.
- NLP Engineer @ Mad Street Den (AI/ML, 201-500, 40mo): Built a content recommendation system serving 10M+ users that combined collaborative filtering with content-based ranking. The system uses item-item similarity (via sentence-transformer embeddings) for cold starts and a gradient-boosted model trained on engagement signals for warm users. Most of my time went into the feature pipeline (~200 features) and the A/B testing infrastructure. The launch improved 7-day retention by 6% and time spent per session by 14%.
_Edu:_ Ph.D Data Science, Delhi College of Engineering (tier_2)
_Signals:_ last_active 2026-05-02, response_rate 0.67, open_to_work False, notice 120d, relocate True, interview_completion 0.94, github 53.5

`tier: ___`  notes: 


---

**model rank #47**

### CAND_0069905  [submission_top]
**Applied ML Engineer** @ Sarvam AI (AI/ML, 51-200) | 6.6y | Bhubaneswar, Odisha, India
_Summary:_ Machine learning engineer with 6.6 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. Along the way I've gotten comfortable with the operational side — A/B testing, drift monitoring, retraining schedules. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Applied ML Engineer @ Sarvam AI (AI/ML, 51-200, 26mo, current): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
- Machine Learning Engineer @ Nykaa (E-commerce, 1001-5000, 13mo): Implemented a RAG-based customer support chatbot integrated with our existing ticketing system. Built the document ingestion pipeline (chunking, embedding via OpenAI embeddings, storing in Pinecone) and the answer-generation layer (initially GPT-4, then a fine-tuned smaller model for cost control). Designed the evaluation framework with both automatic metrics (BLEU, ROUGE) and human-in-the-loop quality scores. Deployment cut average ticket resolution time by 31% for the supported categories.
- Recommendation Systems Engineer @ Observe.AI (AI/ML, 201-500, 39mo): Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Designed the query expansion module that handles vocabulary mismatch between user queries and document terms. Reported search-relevance improvement of 35% over the prior Elasticsearch BM25 setup, validated through human relevance judgments.
_Edu:_ M.E. Computer Engineering, PES University (tier_2)
_Signals:_ last_active 2026-04-21, response_rate 0.78, open_to_work True, notice 90d, relocate True, interview_completion 0.93, github 44.8

`tier: ___`  notes: 


---

**model rank #48**

### CAND_0010257  [submission_top]
**Senior Data Scientist** @ Google (Internet, 10001+) | 6.5y | Noida, Uttar Pradesh, India
_Summary:_ Machine learning engineer with 6.5 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. I care a lot about evaluation rigor — too many teams ship models without offline benchmarks they trust. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Senior Data Scientist @ Google (Internet, 10001+, 37mo, current): Built and operated production ML pipelines using MLflow for experiment tracking, Kubeflow for orchestration, and our internal feature store. My main project was a churn prediction model that's now used by the customer success team to prioritize outreach. Designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. Mentored a junior engineer through their first end-to-end ML project last year.
- Search Engineer @ PharmEasy (HealthTech, 5001-10000, 14mo): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
- Senior Data Scientist @ Google (Internet, 10001+, 26mo): Built a content recommendation system serving 10M+ users that combined collaborative filtering with content-based ranking. The system uses item-item similarity (via sentence-transformer embeddings) for cold starts and a gradient-boosted model trained on engagement signals for warm users. Most of my time went into the feature pipeline (~200 features) and the A/B testing infrastructure. The launch improved 7-day retention by 6% and time spent per session by 14%.
_Edu:_ Ph.D Computer Science, COEP Pune (tier_2)
_Signals:_ last_active 2026-05-13, response_rate 0.72, open_to_work True, notice 120d, relocate True, interview_completion 0.92, github 45.5

`tier: ___`  notes: 


---

**model rank #49**

### CAND_0099806  [submission_top]
**AI Engineer** @ Mad Street Den (AI/ML, 201-500) | 4.6y | Bhubaneswar, Odisha, India
_Summary:_ Machine learning engineer with 4.6 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. I've spent enough time debugging production ranking issues to know which signals matter and which are noise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- AI Engineer @ Mad Street Den (AI/ML, 201-500, 33mo, current): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
- Machine Learning Engineer @ upGrad (EdTech, 1001-5000, 21mo): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
_Edu:_ M.Tech Computer Engineering, IIT Roorkee (tier_1)
_Signals:_ last_active 2026-05-05, response_rate 0.76, open_to_work True, notice 30d, relocate True, interview_completion 0.85, github 86.9

`tier: ___`  notes: 


---

**model rank #50**

### CAND_0096142  [submission_top]
**Applied ML Engineer** @ upGrad (EdTech, 1001-5000) | 5.0y | Hyderabad, Telangana, India
_Summary:_ Machine learning engineer with 5.0 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, my main project for the last 18 months has been the recommendation system that powers our discovery feed. Along the way I've gotten comfortable with the operational side — A/B testing, drift monitoring, retraining schedules. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.
_Career:_
- Applied ML Engineer @ upGrad (EdTech, 1001-5000, 42mo, current): Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself.
- Applied ML Engineer @ BYJU'S (EdTech, 10001+, 18mo): Built a content recommendation system serving 10M+ users that combined collaborative filtering with content-based ranking. The system uses item-item similarity (via sentence-transformer embeddings) for cold starts and a gradient-boosted model trained on engagement signals for warm users. Most of my time went into the feature pipeline (~200 features) and the A/B testing infrastructure. The launch improved 7-day retention by 6% and time spent per session by 14%.
_Edu:_ M.Tech Machine Learning, IIIT Bangalore (tier_1)
_Signals:_ last_active 2026-05-21, response_rate 0.84, open_to_work True, notice 120d, relocate False, interview_completion 0.55, github 80.5

`tier: ___`  notes: 

