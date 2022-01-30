
<!-- [ TEMPLATE ] -->
<template>

    <!-- [ blurred circled ] -->
    <div class="back-blur-circle circle-top"></div>
    <div class="back-blur-circle circle-bottom"></div>

    <!-- [ modal: select user ] -->
    <SelectUser v-if="show_modal" :active_user="active_user" @setUser="setUser" @selectUserModal="selectUserModal" />

    <!-- [ sidebar ] -->
    <Sidebar :page="page" :active_user="active_user" @setPage="setPage" @selectUserModal="selectUserModal" :key="active_user" />

    <section class = 'right-section'>
        <!-- [ header ] -->
        <Header @setPage="setPage" />

        <!-- [ content: pages ] -->
        <Content>
            <Home v-if="page=='Home'" :active_user="active_user" :key="active_user" />
            <CaseStatus v-if="page=='CaseStatus'" :active_user="active_user" :key="active_user" />
        </Content>

        <!-- [ footer ] -->
        <footer>
            &copy; Accenture Investment, 2021 | All rights reserved.
        </footer>
    </section>


</template>


<!-- [ SCRIPTS ] -->
<script>
// [ Partials ]
import Sidebar from './components/partials/Sidebar'
import Header from './components/partials/Header'
import Content from './components/partials/Content'

// [ Pages ]
import CaseStatus from './pages/CaseStatus'
import Home from './pages/Home'

// [ Components ]
import SelectUser from './components/SelectUser'

export default {
    // [ Component name ]
    name: 'App',

    // [ Child components ]
    components: {
        // [ partials ]
        Sidebar,
        Header,
        Content,

        // [ pages ]
        CaseStatus,
        Home,

        // [ other components ]
        SelectUser
    },

    // [ Data ]
    data() {
        return {
            page: 'Home',
            active_user: 'user1',
            show_modal: false
        }
    },

    // [ Methods ]
    methods: {
        setPage( newpage ) {
            this.page = newpage;
        },
        setUser( user ) {
            this.active_user = user;
            setTimeout(() => {
                this.show_modal = false;
            }, 150);
        },
        selectUserModal( open ) {
            this.show_modal = open;
        },
    }
}
</script>

