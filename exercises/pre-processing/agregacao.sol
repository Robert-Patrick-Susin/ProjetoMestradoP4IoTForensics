pragma solidity >=0.4.16 <0.9.0;

contract iot_agregado {
    uint256 public totalPkts; //starts at 0
    // uint256 public totalDevices; //starts at 0 
    address public administrator;
    //structs
    //struct Device {}

    struct aggregacao {
    uint256 id_iot
    uint256 [iot_agregacao];
    uint256 [iot_agregacao];
    uint256 [iot_agregacao];
    }

    aggregacao[] public agregacoes;
    //mappings
    //mapping(uint => Device) public devices;
    constructor() {
        administrator = msg.sender;
    }
    function envia_pkt_agregado(uint256 id_iot, uint256 [iot_agregacao], uint256 [iot_agregacao], uint256 [iot_agregacao]) external {
        // (uint256 id, uint256 val1, uint256 val2, uint256 val3) external {}
        totalPkts += 1;
        agregacoes.push(pkt);
    }
}