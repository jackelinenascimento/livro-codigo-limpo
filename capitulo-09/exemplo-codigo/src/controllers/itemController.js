const itemService = require('../services/itemService');

exports.getItems = (req, res) => {
  const items = itemService.getItems();
  res.json(items);
};

exports.createItem = (req, res) => {
  const newItem = req.body;
  const createdItem = itemService.createItem(newItem);
  res.status(201).json(createdItem);
};