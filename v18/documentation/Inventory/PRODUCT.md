# Product Configuration

- <strong>Units of Measure</strong> : Quantity to specify product amount(meters, yards, killograms).
- <strong>Packaging</strong> : Physical container containing same or different products.
- <strong>Packages</strong> : Fix no. of items of one product. eg. 1 package = 6/12/18 Cans of soda...

## Product Configuration
### Product Type
- In Odoo Goods & Services = Product
- **Sale & Purchase**:
    - Tick Sales if product can be sold to customer.
    - Tick Purchase if it can be purchased.(raw material)
  
- **Goods & Service**:
    - **Good** : eg. Soap. 
      - Menus 
        1.  Inventory
        2. Invoicing Policy : At what point sales process customer as invoiced?
        3. Track Inventory : Track product inside inventory.
           - Tracked : Finished goods, raw materials needed to mfg another good.
           - Untracked : Consumed in short period of time. Essential items like office supplies etc.
             <br>
           - `Forecasted : On Hand Qty + Incoming Shipments - Outgoing Shipments`
            - **Putaway Rules** : Where to store when shipment arrives.
    - **Service** : a repair. **UNTRACKABLE**
    - **Combo** : New car = product, oil change = Service
  
### Units of Measure
- Allow businesses to handle products in different measurement systems and automatically convert between them when needed.
  - Example: Buy in boxes of 12, store in pieces, sell in dozens.
- Odoo can convert UoM to another category if both units are under same category.(Configuration > UoM Categories).
- Base unit acts as default unit in each category.

### Package
- Package is a physical container holding one or more products.
- **Usage** :
  - Grouping products to move in bulk.
  - 