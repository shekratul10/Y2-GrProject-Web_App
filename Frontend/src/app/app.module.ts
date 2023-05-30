import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router'
import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { TelemetryComponent } from './telemetry/telemetry.component';
import { MapComponent } from './map/map.component';
import {HttpClientJsonpModule, HttpClientModule} from '@angular/common/http';
import { ControlPanelComponent } from './control-panel/control-panel.component';
import { BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { MatButtonModule } from '@angular/material/button';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatToolbarModule} from '@angular/material/toolbar';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { MatSnackBarModule, MAT_SNACK_BAR_DEFAULT_OPTIONS } from '@angular/material/snack-bar';
import { MatCardModule} from '@angular/material/card'
import { FrontpageComponent } from './frontpage/frontpage.component';
import { MenubarComponent } from './menubar/menubar.component';
import { ConsoleComponent } from './console/console.component';
import { RoverViewportComponent } from './rover-viewport/rover-viewport.component';

const routes: Routes = [
  {path:'', component:FrontpageComponent},
  {path:'console', component:ConsoleComponent},
  { path: 'dashboard', loadChildren: () => import('./dashboard/dashboard.module').then(m => m.DashboardModule) },
];

@NgModule({
  declarations: [
    AppComponent,
    FrontpageComponent,
    MenubarComponent,
    ConsoleComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes),
    HttpClientModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatToolbarModule,
    MatButtonToggleModule,
    MatSnackBarModule,
    MatCardModule,
    HttpClientJsonpModule
  ],
  providers: [
    {provide: MAT_SNACK_BAR_DEFAULT_OPTIONS, useValue: {duration: 2500}}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
