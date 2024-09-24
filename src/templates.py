template = """
Responde a la siguiente pregunta basándote **únicamente** en el contexto proporcionado. No incluyas información que no esté en el contexto ni inventes datos.

Si el contexto no contiene la información necesaria para responder la pregunta, indica **solo** que no tienes esa información, sin agregar detalles adicionales.

**Pregunta:** {question}

**Contexto:** {context}

Al final, indica de dónde obtuviste la información.
"""
