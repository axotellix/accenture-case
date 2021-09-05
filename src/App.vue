
<!-- [ TEMPLATE ] -->
<template>

    <!-- [ sidebar ] -->
    <Sidebar />

    <section class = 'right-section'>
        <!-- [ header ] -->
        <Header />

        <!-- [ content ] -->
        <Content>
            <CaseStatus />
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
    }
}
</script>

