from eventsourcing.domain.model.entity import EventSourcedEntity, EntityRepository
from eventsourcing.domain.model.events import publish
from quantdsl.domain.services.uuids import create_uuid4


class ContractValuation(EventSourcedEntity):

    class Created(EventSourcedEntity.Created):
        pass

    class Discarded(EventSourcedEntity.Discarded):
        pass

    def __init__(self, market_simulation_id, contract_specification_id, periodisation, approximate_discounting,
                 **kwargs):
        super(ContractValuation, self).__init__(**kwargs)
        self._market_simulation_id = market_simulation_id
        self._contract_specification_id = contract_specification_id
        self._periodisation = periodisation
        self._approximate_discounting = approximate_discounting

    @property
    def market_simulation_id(self):
        return self._market_simulation_id

    @property
    def contract_specification_id(self):
        return self._contract_specification_id

    @property
    def periodisation(self):
        return self._periodisation

    @property
    def approximate_discounting(self):
        return self._approximate_discounting


def start_contract_valuation(contract_specification_id, market_simulation_id, periodisation, approximate_discounting):
    contract_valuation_id = create_contract_valuation_id()
    contract_valuation_created = ContractValuation.Created(
        entity_id=contract_valuation_id,
        market_simulation_id=market_simulation_id,
        contract_specification_id=contract_specification_id,
        periodisation=periodisation,
        approximate_discounting=approximate_discounting,
    )
    contract_valuation = ContractValuation.mutator(event=contract_valuation_created)
    publish(contract_valuation_created)
    return contract_valuation


def create_contract_valuation_id():
    return create_uuid4()


class ContractValuationRepository(EntityRepository):
    pass
