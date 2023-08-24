const ContactList = artifacts.require("ContactList");

module.exports = function(deployer) {
    deployer.deploy(ContactList);
};