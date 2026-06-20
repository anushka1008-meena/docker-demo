{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c1974d7-2039-4857-9a22-a7cfc8f919fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/tmp/ipykernel_473/1387427449.py:4: DeprecationWarning: value_deserializer does not implement kafka.serializer.Deserializer\n",
      "  consumer = KafkaConsumer(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'id': 0, 'name': 'Student-0'}\n",
      "{'id': 1, 'name': 'Student-1'}\n",
      "{'id': 2, 'name': 'Student-2'}\n",
      "{'id': 3, 'name': 'Student-3'}\n",
      "{'id': 4, 'name': 'Student-4'}\n",
      "{'id': 5, 'name': 'Student-5'}\n",
      "{'id': 6, 'name': 'Student-6'}\n",
      "{'id': 7, 'name': 'Student-7'}\n",
      "{'id': 8, 'name': 'Student-8'}\n",
      "{'id': 9, 'name': 'Student-9'}\n",
      "{'id': 0, 'name': 'Student-0'}\n",
      "{'id': 1, 'name': 'Student-1'}\n",
      "{'id': 2, 'name': 'Student-2'}\n",
      "{'id': 3, 'name': 'Student-3'}\n",
      "{'id': 4, 'name': 'Student-4'}\n",
      "{'id': 5, 'name': 'Student-5'}\n",
      "{'id': 6, 'name': 'Student-6'}\n",
      "{'id': 7, 'name': 'Student-7'}\n",
      "{'id': 8, 'name': 'Student-8'}\n",
      "{'id': 9, 'name': 'Student-9'}\n",
      "{'id': 0, 'name': 'Student-0'}\n",
      "{'id': 1, 'name': 'Student-1'}\n",
      "{'id': 2, 'name': 'Student-2'}\n",
      "{'id': 3, 'name': 'Student-3'}\n",
      "{'id': 4, 'name': 'Student-4'}\n",
      "{'id': 5, 'name': 'Student-5'}\n",
      "{'id': 6, 'name': 'Student-6'}\n",
      "{'id': 7, 'name': 'Student-7'}\n",
      "{'id': 8, 'name': 'Student-8'}\n",
      "{'id': 9, 'name': 'Student-9'}\n",
      "{'id': 0, 'name': 'Student-0'}\n",
      "{'id': 1, 'name': 'Student-1'}\n",
      "{'id': 2, 'name': 'Student-2'}\n",
      "{'id': 3, 'name': 'Student-3'}\n",
      "{'id': 4, 'name': 'Student-4'}\n",
      "{'id': 5, 'name': 'Student-5'}\n",
      "{'id': 6, 'name': 'Student-6'}\n",
      "{'id': 7, 'name': 'Student-7'}\n",
      "{'id': 8, 'name': 'Student-8'}\n",
      "{'id': 9, 'name': 'Student-9'}\n",
      "{'id': 0, 'name': 'Student-0'}\n",
      "{'id': 1, 'name': 'Student-1'}\n",
      "{'id': 2, 'name': 'Student-2'}\n",
      "{'id': 3, 'name': 'Student-3'}\n",
      "{'id': 4, 'name': 'Student-4'}\n",
      "{'id': 5, 'name': 'Student-5'}\n",
      "{'id': 6, 'name': 'Student-6'}\n",
      "{'id': 7, 'name': 'Student-7'}\n",
      "{'id': 8, 'name': 'Student-8'}\n",
      "{'id': 9, 'name': 'Student-9'}\n",
      "{'id': 0, 'name': 'Student-0'}\n",
      "{'id': 1, 'name': 'Student-1'}\n",
      "{'id': 2, 'name': 'Student-2'}\n",
      "{'id': 3, 'name': 'Student-3'}\n",
      "{'id': 4, 'name': 'Student-4'}\n",
      "{'id': 0, 'name': 'Student-0'}\n",
      "{'id': 1, 'name': 'Student-1'}\n",
      "{'id': 2, 'name': 'Student-2'}\n",
      "{'id': 3, 'name': 'Student-3'}\n",
      "{'id': 4, 'name': 'Student-4'}\n",
      "{'id': 5, 'name': 'Student-5'}\n",
      "{'id': 6, 'name': 'Student-6'}\n",
      "{'id': 7, 'name': 'Student-7'}\n",
      "{'id': 8, 'name': 'Student-8'}\n",
      "{'id': 9, 'name': 'Student-9'}\n"
     ]
    }
   ],
   "source": [
    "from kafka import KafkaConsumer\n",
    "import json\n",
    "\n",
    "consumer = KafkaConsumer(\n",
    "    \"demo-topic\",\n",
    "    bootstrap_servers=\"kafka:9092\",\n",
    "    auto_offset_reset=\"earliest\",\n",
    "    value_deserializer=lambda x: json.loads(x.decode(\"utf-8\"))\n",
    ")\n",
    "\n",
    "for msg in consumer:\n",
    "    print(msg.value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f27b3957-ad00-46cb-8074-5e9787cdb173",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
