# Google Cloud Storage error-handling
* Custom_retry.py: para cambiar los parámetros que vienen por default por google cloud storage (initial wait time, wait time multiplier per operation, max wait time). 

* Conditional_retry_policy.py: define una clase que, según el error type (429, 500, 502, 503, 504), revisa los parámetros de la API call para chequear si es idempotente y, por ende, es seguro efectuar un retry. 

* Circuit_breaker.py: define una clase que va contabilizando parámetros después de cada retry, de forma tal de decidir si continuar efectuando retries, y en este caso, cada cuánto tiempo y con qué parámetros, o abrir el circuito (ie: no more retries → pasar una fallback function (o no)).
