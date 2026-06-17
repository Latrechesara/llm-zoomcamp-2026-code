from ingest import load_faq_data, build_index

documents = load_faq_data()
index = build_index(documents)

INSTRUCTIONS = """
Your task is to answer questions from the course participants
based on the provided context.

Use the context to find relevant information and provide accurate
answers. If the answer is not found in the context,
respond with "I don't know."
"""

USER_PROMPT_TEMPLATE = """
QUESTION: {question}

CONTEXT:
{context}
""".strip()

class RAGBase:

    def __init__(
        self,
        index,
        llm_client,
        instructions=INSTRUCTIONS,
        prompt_template=USER_PROMPT_TEMPLATE,
        model="llama-3.3-70b-versatile"
    ):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.prompt_template = prompt_template
        self.model = model

    # 1. Added 'self' and switched to 'self.index' and 'self.course'
    def search(self, question, course=None):
        
        
        return self.index.search(
            query=question,
            
            num_results=5
        )

    # 2. Added 'self' so it can be called internally
    def build_context(self, search_results):
        lines = []
        for doc in search_results:
            lines.append(doc["content"])
            lines.append( doc["filename"])
            lines.append("")
        return "\n".join(lines).strip()

    # 3. Added 'self', called 'self.build_context', and used 'self.prompt_template'
    def build_prompt(self, query, search_results):
        context = self.build_context(search_results)
        prompt = self.prompt_template.format(
            question=query, 
            context=context
        )
        return prompt.strip()

    # 4. Added 'self' and replaced global 'client' with instance 'self.llm_client'
    def llm(self, instructions, user_prompt, model=None):
            if model is None:
                model = self.model
                
            message_history = [
                # Swapped 'developer' to 'system' to align with standard API validation
                {"role": "system", "content": instructions},
                {"role": "user", "content": user_prompt}
            ]
            response = self.llm_client.chat.completions.create(
                model=model,
                messages=message_history
            )
            # MODIFY: Return the full response object instead of just the text content
            return response
        
    def rag(self, query, model=None):
        if model is None:
            model = self.model
            
        search_results = self.search(query)
        prompt = self.build_prompt(query, search_results)
        
        # MODIFY: This now receives the complete response object
        response = self.llm(self.instructions, prompt, model=model)
        
        # Extract the fields we need
        answer = response.choices[0].message.content
        usage = response.usage  # Contains prompt_tokens, completion_tokens, total_tokens
        
        # Return both as a tuple
        return answer, usage