<script>
  import Tabletotal from "./Tabletotal.svelte";
  import TableMenu from "./TableMenu.svelte";
  import Router from "svelte-spa-router";
  import TableHeader from "./TableHeader.svelte";
  import Tabletest from "./Tabletest.svelte";

  const routes = {
    "/table": Tabletotal,
    "/table/delete": Tabletotal,
    "/table/test": Tabletest,
    "/table/:userid": Tabletotal,
    "/table/directer/:userid": Tabletotal,
  };
</script>

<div class="row pb-3">
  <div class="menu"><TableMenu /></div>
  <div class="col minwidthheaer">
    <div class="tablesticky mb-2">
      <TableHeader />
    </div>
    <div>
      <Router {routes} />
    </div>
  </div>
</div>

<style>
  .menu {
    width: 15em;
    margin: 0.5em;
  }

  .tablesticky {
    position: sticky;
    top: 0px;
    background-color: white;
    height: 50px;
    padding-top: 5px;
  }

  .minwidthheaer {
    min-width: 1000px;
    width: 1000px;
  }
</style>
