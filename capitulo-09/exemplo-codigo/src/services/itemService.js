// Serviço de Itens
const items = [
    { id: 1, name: 'Item 1' },
    { id: 2, name: 'Item 2' },
    { id: 3, name: 'Item 3' },
  ];
  
  exports.getItems = () => {
    return items;
  };
  
  exports.createItem = (newItem) => {
    items.push(newItem);
    return newItem;
  };