/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl"
import { registry } from '@web/core/registry'
import { rpc } from "@web/core/network/rpc"
import { useService } from "@web/core/utils/hooks"
import { listView} from "@web/views/list/list_view"
import { ListController } from "@web/views/list/list_controller"
import { Dialog } from "@web/core/dialog/dialog"

export class CustomerQuickInfoDialog extends Component{
    static template = "owl_customer_quick_info.CustomerQuickInfoDialog"
    static components = { Dialog }

    setup(){
        super.setup()
        this.state = useState({ customers : []})
        onWillStart(async ()=>{
            this.state.customers = await this.fetchCustomers()
        })
    }

    async fetchCustomers(){
        try{
            const customers = await rpc("/customers")
            console.log(customers)
            return customers
        }catch(e){
            console.log("Error: ", e)
            return []
        }
    }

    close(){
        this.props.close()
    }
}

export class PartnerListController extends ListController{
    setup(){
        super.setup()
        this.dialog = useService("dialog")
    }

    async openQuickInfo(){
        this.dialog.add(CustomerQuickInfoDialog, {}, {
            title : "Customers Quick Info"
        })
    }
}

export const partnerListView = {
    ...listView,
    Controller : PartnerListController,
    buttonTemplate : "owl_customer_quick_info.PartnerListController.Buttons"
}

registry.category("views").add("customer_quick_info", partnerListView)