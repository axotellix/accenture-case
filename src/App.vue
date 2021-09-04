
<!-- [ TEMPLATE ] -->
<template>

    <!-- [ sidebar ] -->
    <Sidebar />

    <section class = 'right-section'>
        <!-- [ header ] -->
        <Header />

        <!-- [ content ] -->
        <Content />
    </section>


</template>


<!-- [ SCRIPTS ] -->
<script>
import Sidebar from './components/partials/Sidebar'
import Header from './components/partials/Header'
import Content from './components/partials/Content'

export default {
    name: 'App',
    components: {
        Sidebar,
        Header,
        Content,
    }
}
</script>

