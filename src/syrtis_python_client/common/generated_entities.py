from __future__ import annotations

from syrtis_python_client.entity.card import Card
from syrtis_python_client.entity.card_message import CardMessage
from syrtis_python_client.entity.card_relation import CardRelation
from syrtis_python_client.entity.chunk import Chunk
from syrtis_python_client.entity.document import Document
from syrtis_python_client.entity.environment import Environment
from syrtis_python_client.entity.job import Job
from syrtis_python_client.entity.message import Message
from syrtis_python_client.entity.message_stamp import MessageStamp
from syrtis_python_client.entity.node import Node
from syrtis_python_client.entity.request import Request
from syrtis_python_client.entity.scenario import Scenario
from syrtis_python_client.entity.session import Session
from syrtis_python_client.entity.slot import Slot
from syrtis_python_client.entity.slot_config import SlotConfig
from syrtis_python_client.entity.slot_message import SlotMessage
from syrtis_python_client.entity.slot_message_stamp import SlotMessageStamp
from syrtis_python_client.entity.slot_relation import SlotRelation
from syrtis_python_client.entity.template import Template
from syrtis_python_client.entity.timezone import Timezone
from syrtis_python_client.entity.user import User


generated_entities = [
    Card,
    CardMessage,
    CardRelation,
    Chunk,
    Document,
    Environment,
    Job,
    Message,
    MessageStamp,
    Node,
    Request,
    Scenario,
    Session,
    Slot,
    SlotConfig,
    SlotMessage,
    SlotMessageStamp,
    SlotRelation,
    Template,
    Timezone,
    User,
]
all_entities = list(generated_entities)
