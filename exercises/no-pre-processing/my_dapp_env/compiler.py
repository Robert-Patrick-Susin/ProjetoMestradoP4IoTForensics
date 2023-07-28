import solcx
solcx.compile_files(
    ["test.sol"],
    output_values=["abi", "bin-runtime"],
    solc_version="0.8.21"
)
{
    '<stdin>:Foo': {
        'abi': [{'inputs': [], 'name': 'bar', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}],
        'bin-runtime': '6080604052348015600f57600080fd5b506004361060285760003560e01c8063febb0f7e14602d575b600080fd5b60336035565b005b56fea26469706673582212203cfdbce82ee8eab351107edac2ebb9dbe5c1aa8bd26609b0eedaa105ed3d4dce64736f6c63430007000033'
    }
}