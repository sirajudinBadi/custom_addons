/** @odoo-module **/
import { rpc } from "@web/core/network/rpc";
import { registry } from "@web/core/registry";
import { useState, Component, onWillStart } from "@odoo/owl";
export class WebOwlComponentSnippet extends Component {
    static template = "your_module_name.snippet_xml";
    setup() {
        this.state = useState({
            data: [],
        });
        onWillStart(async () => {
            this.state.data = await rpc("/get_product_details");
        });
    }
}
registry.category("public_components").add("your_module_name.snippet", WebOwlComponentSnippet);
