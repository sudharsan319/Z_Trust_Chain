// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AuthEvent {
    struct Event {
        string prevHash;
        string nonce;
        string did;
        uint256 timestamp;
        string signature;
        string policyHash;
    }

    Event[] public events;

    event AuthLogged(
        string prevHash,
        string nonce,
        string did,
        uint256 timestamp,
        string signature,
        string policyHash
    );

    function logEvent(
        string memory prevHash,
        string memory nonce,
        string memory did,
        uint256 timestamp,
        string memory signature,
        string memory policyHash
    ) public {
        events.push(Event(prevHash, nonce, did, timestamp, signature, policyHash));
        emit AuthLogged(prevHash, nonce, did, timestamp, signature, policyHash);
    }

    function logEventsBatch(Event[] memory eventsBatch) public {
        for (uint i = 0; i < eventsBatch.length; i++) {
            events.push(eventsBatch[i]);
            emit AuthLogged(
                eventsBatch[i].prevHash,
                eventsBatch[i].nonce,
                eventsBatch[i].did,
                eventsBatch[i].timestamp,
                eventsBatch[i].signature,
                eventsBatch[i].policyHash
            );
        }
    }

    function getEventCount() public view returns (uint256) {
        return events.length;
    }

    function getEvent(uint256 index) public view returns (
        string memory, string memory, string memory, uint256, string memory, string memory
    ) {
        Event memory e = events[index];
        return (e.prevHash, e.nonce, e.did, e.timestamp, e.signature, e.policyHash);
    }
}
