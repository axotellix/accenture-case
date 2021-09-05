
<!-- [ TEMPLATE ] -->
<template>

    <!-- [ sidebar ] -->
    <Sidebar :page="page" />

    <section class = 'right-section'>
        <!-- [ header ] -->
        <Header @setPage="setPage" />

        <!-- [ content: pages ] -->
        <Content>
            <Home v-if="page=='Home'"  />
            <CaseStatus v-if="page=='CaseStatus'" />
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
    },

    // [ Data ]
    data() {
        return {
            page: 'Home'
        }
    },

    // [ Methods ]
    methods: {
        setPage( newpage ) {
            this.page = newpage;
        }
    }
}
</script>

