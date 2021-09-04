
<!-- [ TEMPLATE ] -->
<template>

    <!-- [ sidebar ] -->
    <Sidebar />

    <!-- [ header ] -->
    <Header />

    <!-- [ content ] -->
    <Content />


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

