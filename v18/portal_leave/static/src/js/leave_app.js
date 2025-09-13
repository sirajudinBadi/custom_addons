/** @odoo-module **/

import { Component, mount, useState, onWillStart } from "@odoo/owl";
import { jsonrpc } from "@web/core/network/rpc_service";
//import { Component, mount } from "@odoo/owl";

class LeaveApp extends Component {
    static template = "<div>✅ Owl App Loaded!</div>";
}

export function startLeaveApp() {
    console.log("✅ startLeaveApp() called");
    mount(LeaveApp, document.getElementById("portal_leave_app_root"));
}


class LeaveList extends Component {
    setup() {
        this.state = useState({ leaves: [] });
        onWillStart(async () => {
            this.state.leaves = await jsonrpc("/my/leaves/data");
        });
    }

    goToForm() {
        this.env.router.navigate("apply");
    }
}
LeaveList.template = "portal_leave.LeaveList";


class LeaveForm extends Component {
    setup() {
        this.state = useState({
            leaveTypes: [],
            formData: {
                holiday_status_id: "",
                request_date_from: "",
                request_date_to: "",
                description: "",
            },
        });
        onWillStart(async () => {
            this.state.leaveTypes = await jsonrpc("/my/leaves/leave_types");
        });
    }

    get isUnpaid() {
        const selected = this.state.leaveTypes.find(
            (t) => t.id == this.state.formData.holiday_status_id
        );
        return selected?.name === "Unpaid";
    }

    updateField(ev) {
        this.state.formData[ev.target.name] = ev.target.value;
    }

    async submitForm(ev) {
        ev.preventDefault();
        await jsonrpc("/my/leaves/submit", this.state.formData);
        this.env.router.navigate("list"); // go back after submit
    }
}
LeaveForm.template = "portal_leave.LeaveForm";


class LeaveApp extends Component {
    setup() {
        this.state = useState({ currentRoute: "list" });
        this.env.router = {
            navigate: (route) => (this.state.currentRoute = route),
        };
    }

    get CurrentScreen() {
        return this.state.currentRoute === "list" ? LeaveList : LeaveForm;
    }
}
LeaveApp.template = "portal_leave.LeaveApp";

export async function startLeaveApp() {
    mount(LeaveApp, document.body);
}
