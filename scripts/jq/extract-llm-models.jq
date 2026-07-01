# LangChain / AI model nodes → provider + model.
# n8n LangChain nodes live under @n8n/n8n-nodes-langchain.*
#
# Model handling notes:
# - .parameters.model can be a plain string OR a "resource locator" object
#   {__rl: true, value: "<id>", mode: "list", cachedResultName: "<friendly>"}.
# - Different langchain nodes put the model at different paths (.model / .modelName / .options.modelName).

def unwrap_model:
  if type == "object" then
    (.value // .cachedResultName // null)
  elif type == "string" then
    .
  else null
  end;

def provider_from_type($t):
  if   ($t | test("openAi|OpenAi"))         then "openai"
  elif ($t | test("anthropic|Anthropic"))   then "anthropic"
  elif ($t | test("googleGemini|Google"))   then "google"
  elif ($t | test("groq|Groq"))             then "groq"
  elif ($t | test("ollama|Ollama"))         then "ollama"
  elif ($t | test("mistral|Mistral"))       then "mistral"
  elif ($t | test("cohere|Cohere"))         then "cohere"
  elif ($t | test("azureOpenAi|AzureOpen")) then "azure-openai"
  else null end;

[
  .nodes[]?
  | . as $n
  | select($n.type | startswith("@n8n/n8n-nodes-langchain."))
  | select(
      $n.type | test("(lmChat|lm[A-Z]|chatModel|embeddings|openAi|anthropic|google|groq|ollama|mistral|cohere|openAiAssistant)"; "i")
    )
  | {
      node_id: $n.id,
      node_name: $n.name,
      node_type: $n.type,
      provider: provider_from_type($n.type),
      model: (
        ($n.parameters.model | unwrap_model)
        // ($n.parameters.modelName | unwrap_model)
        // ($n.parameters.options.modelName | unwrap_model)
        // null
      )
    }
] | sort_by(.node_id)
